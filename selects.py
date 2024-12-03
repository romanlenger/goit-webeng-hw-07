from sqlalchemy import func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from tables import Student, Grade, Subject, Group, Teacher


async def select_1(session: AsyncSession):
    result = await session.execute(
        session.query(
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        )
        .join(Grade.student)
        .group_by(Student.id)
        .order_by(desc('avg_grade'))
        .limit(5)
    )
    return result.fetchall()


async def select_2(session: AsyncSession, subject_name: str):
    result = await session.execute(
        session.query(
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        )
        .join(Grade.student)
        .join(Grade.subject)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(desc('avg_grade'))
        .limit(1)
    )
    return result.fetchone()


async def select_3(session: AsyncSession, subject_name: str):
    result = await session.execute(
        session.query(
            Group.name,
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        )
        .join(Group.students)
        .join(Student.grades)
        .join(Grade.subject)
        .filter(Subject.name == subject_name)
        .group_by(Group.id)
    )
    return result.fetchall()


async def select_4(session: AsyncSession):
    result = await session.execute(
        session.query(
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        )
    )
    return result.scalar()


async def select_5(session: AsyncSession, teacher_name: str):
    result = await session.execute(
        session.query(Subject.name)
        .join(Subject.teacher)
        .filter(Teacher.fullname == teacher_name)
    )
    return result.fetchall()


# Знайти список студентів у певній групі.
async def select_6(session: AsyncSession, group_name: str):
    result = await session.execute(
        session.query(Student.fullname)
        .join(Student.group)
        .filter(Group.name == group_name)
    )
    return result.fetchall()


async def select_7(session: AsyncSession, group_name: str, subject_name: str):
    result = await session.execute(
        session.query(
            Student.fullname,
            Grade.grade,
            Grade.date_received
        )
        .join(Student.grades)
        .join(Student.group)
        .join(Grade.subject)
        .filter(Group.name == group_name, Subject.name == subject_name)
    )
    return result.fetchall()


async def select_8(session: AsyncSession, teacher_name: str):
    result = await session.execute(
        session.query(
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        )
        .join(Grade.subject)
        .join(Subject.teacher)
        .filter(Teacher.fullname == teacher_name)
    )
    return result.scalar()


async def select_9(session: AsyncSession, student_name: str):
    result = await session.execute(
        session.query(Subject.name)
        .join(Grade.subject)
        .join(Grade.student)
        .filter(Student.fullname == student_name)
        .distinct()
    )
    return result.fetchall()


async def select_10(session: AsyncSession, student_name: str, teacher_name: str):
    result = await session.execute(
        session.query(Subject.name)
        .join(Grade.subject)
        .join(Grade.student)
        .join(Subject.teacher)
        .filter(
            Student.fullname == student_name,
            Teacher.fullname == teacher_name
        )
        .distinct()
    )
    return result.fetchall()