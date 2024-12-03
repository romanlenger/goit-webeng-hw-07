import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from selects import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10

DATABASE_URL = "postgresql+asyncpg://postgres:mysecretpassword@localhost:5432/my_database"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def run_queries():
    async with async_session() as session:
        print("Запит 1: Топ 5 студентів з найбільшим середнім балом")
        result = await select_1(session)
        for row in result:
            print(row)

        print("\nЗапит 2: Найкращий студент з предмета")
        result = await select_2(session, subject_name="Math")
        print(result)

        print("\nЗапит 3: Середній бал у групах")
        result = await select_3(session, subject_name="History")
        for row in result:
            print(row)

        print("\nЗапит 4: Середній бал на потоці")
        result = await select_4(session)
        print(result)

        print(await select_5(session))
        print(await select_6(session))
        print(await select_7(session))
        print(await select_8(session))
        print(await select_9(session))
        print(await select_10(session))

asyncio.run(run_queries())
