import psycopg2
import os
import pytest
from sshtunnel import SSHTunnelForwarder
from dotenv import load_dotenv
from config.environment_allure import EnvironmentAllure

load_dotenv()


ssh_host = '16.170.215.221'
ssh_port = 22
ssh_user = os.getenv('SSH_USER')
ssh_key = 'SSH_KEY'
ssh_pass = os.getenv('SSH_PASSW')

db_host = '127.0.0.1'
db_port = 5432
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = 'training_store'


@pytest.fixture()
def cursor(request):
    print('SSH_KEY')
    EnvironmentAllure.create_environment()
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=ssh_key,
            ssh_password=ssh_pass,
            remote_bind_address=(db_host, db_port)
    ) as tunnel:
        conn = psycopg2.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=tunnel.local_bind_port,
            database=db_name
        )
        cursor = conn.cursor()
        request.cls.cursor = cursor
        yield cursor
        cursor.close()
        conn.close()
