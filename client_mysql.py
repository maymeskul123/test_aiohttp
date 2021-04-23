from sqlalchemy import create_engine
import os

class Client_MySQL:
    def __init__(self):
        #self.mybase = create_engine(f'mysql+mysqldb://{user}:{password}@)localhost/test_base')
        self.mybase = create_engine(f'mysql+mysqldb://user:password@)localhost/test_base')

    def insert(self, data):
        self.mybase.execute(f"""insert into users(name, age, city) values ({data['name']}, {data['age']}, {data['city']})""")

