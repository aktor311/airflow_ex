from airflow.models.connection import Connection
from airflow.sensors.base import BaseSensorOperator
import psycopg2 as pg
import pandas.io.sql as psql

class CheckTableSensor(BaseSensorOperator):
    poke_context_fields = ['conn', 'table_name']

    def __init__(self, conn: Connection, table_name: str, *args, **kwargs):
        self.conn = conn
        self.table_name = table_name
        super(CheckTableSensor, self).__init__(*args, **kwargs)

    def poke(self, context):
        connection = pg.connect(f"host={self.conn.host} dbname={self.conn.schema} user={self.conn.login} password={self.conn.password}")
        df_currency = psql.read_sql(f'SELECT * FROM {self.table_name} LIMIT 1', connection)
        if len(df_currency) > 0:
            return True
        else:
            return False