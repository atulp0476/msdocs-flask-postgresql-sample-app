import os

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=conn_str_params['jcejattqrt'],
    dbpass=conn_str_params['6yVbHaagzbkTGY$l'],
    dbhost=conn_str_params['atuldemowebapp-server.postgres.database.azure.com'],
    dbname=conn_str_params['atuldemowebapp-database']
)