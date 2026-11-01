import gvm

from gvm.connections import UnixSocketConnection
from gvm.protocols.latest import Gmp
from gvm.transforms import EtreeCheckCommandTransform
from gvm.errors import GvmError


path = '/var/lib/docker/volumes/greenbone-community-edition_gvmd_socket_vol/_data/gvmd.sock';
connection = UnixSocketConnection(path=path);

with GMP(connection=connection) as gmp:
  response = gm.get_verison();
  print(response);
