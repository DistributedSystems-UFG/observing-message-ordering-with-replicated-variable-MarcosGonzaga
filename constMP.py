#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.7.180','172.31.2.162','172.31.2.145','172.31.12.160','172.31.0.48']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
PEERS_SAME_REGION = ['52.21.65.56','34.195.96.130','54.221.58.118','52.4.144.234','44.222.19.125']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['52.21.65.56','34.195.96.130','54.221.58.118','52.88.207.23','44.239.117.195']


PEER_UDP_PORT = 4678
PEER_TCP_PORT = 5679
N = 5   # Number of peers
SERVER_ADDR ='52.21.65.56'
SERVER_PORT = 5678

# Number of valid operations to call
NUM_OPS = 2

# List of operations
ops = ['deposit', 'interest']

# Ranges of values
depositRange = [1, 10]
interestRange = [1, 2]
