import datetime

from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from models import Category, User, Advert
from models.adverts import District, Region
from models.base import engine
from models.courses import Course

# Base.metadata.create_all(engine)

with Session(engine) as session:
    # courses = [
    #     {
    #         "id": 1,
    #         "name": "Programming",
    #         "updated_at": datetime.datetime.now()
    #     },
    #     {
    #         "id": 2,
    #         "name": "English",
    #         "updated_at": datetime.datetime.now()
    #     },
    #     {
    #         "id": 3,
    #         "name": "Math",
    #         "updated_at": datetime.datetime.now()
    #     }
    # ]

    # students = [
    #     {
    #         "id": 1,
    #         "first_name": "Ali",
    #         "phone": "998901001515",
    #         "updated_at": datetime.datetime.now()
    #     },
    #     {
    #         "id": 2,
    #         "first_name": "Shokir",
    #         "phone": "998901002020",
    #         "updated_at": datetime.datetime.now()
    #     },
    #     {
    #         "id": 3,
    #         "first_name": "Valijon",
    #         "phone": "998905005050",
    #         "updated_at": datetime.datetime.now()
    #     }
    # ]

    # query = insert(User).values(students)
    # query = insert(Course).values(courses)

    # Ali - Math, English
    # Valijon - English, Programming
    # Shokir - Math, English, Programming

    query = select(User).filter(User.id == 1)
    student = session.scalar(query)
    print(student, student.courses)

    # query = select(Course).filter(Course.id == 2) # English
    # english_course = session.scalar(query)
    #
    # query = select(Course).filter(Course.id == 3) # Math
    # math_course = session.scalar(query)
    # print(english_course)
    # print(math_course)

    # student.courses.append(math_course)
    # student.courses.append(english_course)
    #
    # session.commit()


    # session.execute(query)
    # session.commit()

    # query = select(Region)
    # regions = session.scalars(query)
    #
    # for region in regions:
    #     print(region.name, region.districts)

    # data = [
    #     {
    #         'id': 1,
    #         'name': 'Texnika',
    #         'slug': 'texnika'
    #     }
    # ]
    # query = insert(Category).values(data)
    # session.execute(query)
    # session.commit()

# m2m
# o2m
# o2o

# Task
# 1. kurs crud
# 2. student crud

"""
Menyular
1. kurs qo'shish
2. kurs o'chirish
3. kursni o'zgartirish
4. kurslarni ko'rish
5. student qo'shish
6. student o'chirish
7. studentni o'zgartirish
8. studentlarni ko'rish
0. exit

Homework

Menyular
1. kurs qo'shish
2. kurs o'chirish
3. kursni o'zgartirish
4. kurslarni ko'rish
5. student qo'shish
6. student o'chirish
7. studentni o'zgartirish
8. kursga student qo'shish
9. kursdan studentni o'chirish
10. kursdan kursga ko'chirish

"""

