from sqlalchemy.orm import sessionmaker
from models import engine, Supervisor
import click
from faker import Faker

fake = Faker()

""" Using click CLI Library to get and map user input to the DataBase """
# @click.command()
# @click.option("--count", default=1)
# @click.option("--super_id", prompt="Supervisor ID", type=int)
# @click.option("--super_name", prompt="Name")
# @click.option("--super_email", prompt="Email")
# @click.option("--super_major", prompt="Major")

def supervisor_handler(count, super_id, super_name, super_email, super_major):
    for _ in range(count):
        # click.echo("Sup ID: %d" % id)
        # click.echo("Name: %s" % name)
        # click.echo("Email: %s" % email)
        # click.echo("Major: %s" % major)
        sup = {"ID": super_id, "name": super_name, "email": super_email, "major": super_major}
        print(sup)

        new_supervisor = Supervisor(sup_id = super_id, name = super_name, email = super_email, major = super_major)

        session.add(new_supervisor)
        session.commit()
        

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    # supervisor_handler()
    pass

""" CREATE """
# filling DB with initial set of data C
supervisor1 = Supervisor(sup_id = 1000, name="Khalifa Muyideen", email="kmuyideen@outlook.com", major="Software Engineering")
supervisor2 = Supervisor(sup_id = 1001, name="Abdi Rashid", email="abdulrashid@gmail.com", major="Product Design")
supervisor3 = Supervisor(sup_id = 1002, name=fake.name(), email=fake.email(), major="Data Science")
supervisor4 = Supervisor(sup_id = 1003, name="Emma Maart", email="emmamaart@outlook.com", major="Cybersecurity")
# session.add_all([supervisor1, supervisor2, supervisor3, supervisor4])
# session.commit()

""" READ """
# supervisors_list = session.query(Supervisor)
# print([sup for sup in supervisors_list])
# for sups in supervisors_list:
#     print(sups)

""" using OOP """
class supervisor_data_query:
    def __init__(self):
        pass
    
    # READ
    def get_all_supervisors_data(self):
        all_supervisors = session.query(Supervisor).all() #.all() returns a list []
        for supervisor in all_supervisors:
            print(supervisor)   
            pass     
        # print(all_supervisors)
        pass
    
    # DELETE
    def delete_supervisor(self, name):
        self.name = name
        for supervisor in session.query(Supervisor).all():
            if supervisor.name == name:
                session.delete(supervisor)
                session.commit()
                
    # UPDATE
    def update_supervisor_data(self, new_major):
        for supervisor in session.query(Supervisor).all(): #working with a list to update supervisor
            if supervisor.sup_id == 1001:
                supervisor.major = new_major
        session.commit()
        pass
    
sups = supervisor_data_query()
sups.get_all_supervisors_data()

""" UPDATE """
# for supervisor in session.query(Supervisor).all(): #working with a list to update supervisor
#     if supervisor.sup_id == 1001:
#         supervisor.major = "DevOps Engineering" 
# session.commit()
sups.update_supervisor_data("DevOps Engineering")

""" DELETE """
sups.delete_supervisor("Troy Mendoza")

#stud