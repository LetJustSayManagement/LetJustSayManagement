import gvm
import time

from gvm.connections import UnixSocketConnection
from gvm.protocols.latest import Gmp
from gvm.transforms import EtreeCheckCommandTransform
from gvm.errors import GvmError
from lxml import etree
path = '/var/lib/docker/volumes/greenbone-community-edition_gvmd_socket_vol/_data/gvmd.sock';

def OpenvasScan(IPaddr):
  connection = UnixSocketConnection(path=path);

  with Gmp(connection=connection, transform = EtreeCheckCommandTransform()) as gmp:
    gmp.authenticate("admin","admin");
    Run_Report = gmp.start_task("ASM Scanner Prof")
    Trying = 0
    while True:
      Report  = gmp.get_task(Task_ID)
      Task_Status = Report.find(".//status").text
      print(Task_Status)
      if Task_Status == "Done":
        break
      elif Task_Status in ["Stopped", "Interrupted"]:
        raise Exception(f"OpenVAS scan ended with status: {Task_Status}")
      Trying +=1;
      if  Trying >= 120:
        raise TimeoutError("this Scan has timed out")
      time.sleep(60)
    Report_ID = Report.find(".//last_report/report").get("id")
    Finish_Report = gmp.get_report(report_id=Report_ID)
    Clean_Report = etree.tostring(Finish_Report,pretty_print=True).decode()
    return Finish_Report






