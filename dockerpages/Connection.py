from docker import Client
from .IP import IP
#please import this file in all the modules you write to establish the connection with the remote Machine
remote_Machine = Client(base_url='tcp://'+IP+':2375')
