import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from tables import Student, Teacher, Subject, Group, Grade
import random

DATABASE_URL = "postgresql+asyncpg://postgres:mysecretpassword@localhost:5432/my_database"

fake = Faker()

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def create_data():
    async with async_session() as session:
        async with session.begin():

            groups = [Group(name=fake.bothify(text="Group-##")) for _ in range(3)]
            session.add_all(groups)
            await session.commit()

            teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
            session.add_all(teachers)
            await session.commit()

            subjects = [Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(8)]
            session.add_all(subjects)
            await session.commit()

            students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(30)]
            session.add_all(students)
            await session.commit()

            grades = []
            for student in students:
                for subject in subjects:
                    for _ in range(random.randint(5, 20)):
                        grade = Grade(
                            grade=random.uniform(1, 12),
                            date=fake.date_between(start_date="-2y", end_date="today"),
                            student=student,
                            subject=subject
                        )
                        grades.append(grade)
            session.add_all(grades)
            await session.commit()

asyncio.run(create_data())
