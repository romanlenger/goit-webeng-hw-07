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
