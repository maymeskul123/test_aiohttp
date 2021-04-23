import sqlalchemy as db

class Client_MySQL:
    def __init__(self, user, password):
        self.mybase = db.create_engine(f'mysql+mysqldb://{user}:{password}@localhost:3306/test_base')

    def insert(self, data):
        self.mybase.execute(f"""insert into users(name, age, city) values (\'{data['name']}\', \'{data['age']}\', \'{data['city']}\')""")



