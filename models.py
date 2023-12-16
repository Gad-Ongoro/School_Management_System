from sqlalchemy import create_engine, Table, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Phase(Base):
    __tablename__ = "phases"

    phase_id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50))
    sup_id = Column(Integer())

    students = relationship("Student", backref="phase")

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50))
    sup_id = Column(Integer())

    students = relationship("Student", backref=("course"))
    #duration = Column(String(50))

class Supervisor(Base):
    __tablename__ = "supervisors"

    sup_id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    major = Column(String(50))

    students = relationship('Student', backref=('supervisor'))

class Student(Base):
    __tablename__ = "students"

    stud_id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    reg_id = Column(String(50))
    status = Column(String(50))
    course_id = Column(Integer(), ForeignKey("courses.course_id"))
    phase = Column(Integer(), ForeignKey("phases.phase_id"))
    sup_id = Column(Integer(), ForeignKey('supervisors.sup_id'))

engine = create_engine('sqlite:///school_management.db')
Base.metadata.create_all(engine)