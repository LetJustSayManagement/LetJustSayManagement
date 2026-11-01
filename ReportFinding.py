import json
from datetime import datetime
from OSQueryMonitoring import (get_listening_ports,get_processes,get_users,pretty)
from NmapScanning import NmapScanning
from OpenvasScan import OpenvasScan

Now = datetime.datetime.now().strftime("%a,%b,%d,%Y,%H:%M:%S")

