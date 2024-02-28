from sqlalchemy import create_engine
from sqlalchemy import text
import os

#print(os.environ['MYSQL_ROOT_PASSWORD'])
engine = create_engine('mysql+pymysql://root:'+os.environ['MYSQL_ROOT_PASSWORD']+'@try_docker_sql:3306/'+os.environ['MYSQL_DATABASE'])

query = "SHOW DATABASES"

with engine.connect() as connection:
    result = connection.execute(text(query))
    for row in result:
        print(row)

#print(result)