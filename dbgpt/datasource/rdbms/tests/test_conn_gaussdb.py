import sys
import os
from sqlalchemy import text

current_dir = os.path.dirname(os.path.abspath(__file__))

project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..', '..'))
sys.path.insert(0, project_root)

from dbgpt.datasource.rdbms.conn_gaussdb import GaussDBConnector

def test_connection():
    connector = GaussDBConnector.from_uri_db(
        host='192.168.0.164',
        port=8000,
        user='root',
        pwd='Lfh20050311',
        db_name='postgres',
        sslmode='require'          # 根据需要设置
    )
    try:
        result = connector.session.execute(text("SELECT version();"))
        print("Connection successful!")
        print("GaussDB Version:", result.fetchone()[0])
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    test_connection()