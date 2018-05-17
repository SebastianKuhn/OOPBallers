from sshtunnel import SSHTunnelForwarder
import MySQLdb as db
import pandas as pd


# ssh variables
host = '52.xx.xx.xx'
localhost = '127.0.0.1'
ssh_username = 'ubuntu'
ssh_private_key = '/path/to/key.pem'

# database variables
user='root'
password='oop1234'
database='oop'

def query(q):
    with SSHTunnelForwarder(
            (host, 22),
            ssh_username=ssh_username,
            ssh_private_key=ssh_private_key,
            remote_bind_address=(localhost, 3306)
    ) as server:
        conn = db.connect(host=localhost,
                          port=server.local_bind_port,
                          user=user,
                          passwd=password,
                          db=database)
        return pd.read_sql_query(q, conn)