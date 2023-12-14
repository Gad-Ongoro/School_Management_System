from faker import Faker
import random
from sqlalchemy.orm import sessionmaker
from models import engine, Student, Supervisor, Course, Phase

class sup_user_input:
    def __init__(self, sup_id, name, email, major):
        self.sup_id = sup_id
        self.name = name
        self.email = email
        self.major = major

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    sup = sup_user_input(sup_id = int(input("Id: ")), name=input("Name: "), email=input("Email: "), major=input("Major: "))

    supervisor4 = Supervisor(sup)
    
    pass

# supervisor1 = Supervisor(sup_id = 1, name="Khalifa", email="kmuyeeden@gmail.com", major="Software Engineering")
# supervisor2 = Supervisor(sup_id = 2, name="Abdul", email="abdul@gmail.com", major="Science")
    
# supervisor3 = 

# session.add_all([supervisor1, supervisor2])

session.add_all([supervisor4])
session.commit()