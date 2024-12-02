from sqlalchemy import String, Integer, ForeignKey, Date, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Group(Base):
    __tablename__ = 'groups'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    
    students: Mapped[list["Student"]] = relationship("Student", back_populates="group")


class Student(Base):
    __tablename__ = 'students'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fullname: Mapped[str] = mapped_column(String, nullable=False)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey('groups.id'))
    
    group: Mapped["Group"] = relationship("Group", back_populates="students")
    grades: Mapped[list["Grade"]] = relationship("Grade", back_populates="student")


class Teacher(Base):
    __tablename__ = 'teachers'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fullname: Mapped[str] = mapped_column(String, nullable=False)
    
    subjects: Mapped[list["Subject"]] = relationship("Subject", back_populates="teacher")


class Subject(Base):
    __tablename__ = 'subjects'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey('teachers.id'))
    
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="subjects")
    grades: Mapped[list["Grade"]] = relationship("Grade", back_populates="subject")


class Grade(Base):
    __tablename__ = 'grades'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    grade: Mapped[float] = mapped_column(Float, nullable=False)
    date: Mapped[Date] = mapped_column(Date)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey('students.id'))
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey('subjects.id'))
    
    student: Mapped["Student"] = relationship("Student", back_populates="grades")
    subject: Mapped["Subject"] = relationship("Subject", back_populates="grades")
