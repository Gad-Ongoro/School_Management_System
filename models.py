from sqlalchemy import create_engine, Table, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    sup_id = Column(Integer())

    student = relationship("Student", backref=("course"))
    #duration = Column(String(50))



class Supervisor(Base):
    __tablename__ = "supervisors"

    sup_id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    major = Column(String(50))

    student = relationship('Student', backref=('supervisor'))

class Student(Base):
    __tablename__ = "students"

    stud_id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    reg_id = Column(String(50))
    status = Column(String(50))
    phase = Column(String(50))
    sup_id = Column(Integer(), ForeignKey('supervisors.sup_id'))
    course_id = Column(Integer(), ForeignKey("courses.course_id"))

class Phase(Base):
    __tablename__ = "phases"

    phase_id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    sup_id = Column(Integer())

engine = create_engine('sqlite:///school_management.db')
Base.metadata.create_all(engine)