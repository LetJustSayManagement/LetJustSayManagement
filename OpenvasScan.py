import gvm

from gvm.connections import UnixSocketConnection
from gvm.protocols.latest import Gmp
from gvm.transforms import EtreeCheckCommandTransform
from gvm.errors import GvmError

Port_List_ID = "730ef368-57e2-11e1-a90f-406186ea4fc5";
Config_ID = "daba56c8-73ec-11df-a475-002264764cea";
Scanner_ID = "08b69003-5fc2-4037-a479-93b440211c73";

path = '/var/lib/docker/volumes/greenbone-community-edition_gvmd_socket_vol/_data/gvmd.sock';

def OpenvasScan(IPaddr):
  connection = UnixSocketConnection(path=path);

  with Gmp(connection=connection, transform = EtreeCheckCommandTransform()) as gmp:
    gmp.authenticate("admin","admin");
    Target = gmp.create_target(name = "ASM target", hosts = [IPaddr], port_list_id = Port_list_ID);
    Target_ID = Target.get("id");
    Task = gmp.create_task(name ="ASM Scanner",config_id =Config_ID,target_id = Target_ID,scanner_id =Scanner_ID);
    Task_ID = Task.get("id");
    Report = gmp.start_task(Task_ID)

  return Report 
