from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User
from models.base import engine


#

"""
Film(id, title, description, release_year), Category(id, name)
1. film qoshish
2. film o'chirish
3. film o'zgartirish
4. film ni korish
5. category qo'shish
6. category o'chirish
7. category o'zgartirish
8. category ni korish

"""
with Session(engine) as session:
    pass
    # query = select(User.id, User.first_name, User.last_name).where(User.first_name.icontains('ali'))
    # for user in session.scalars(query):
    #     print(user.id, user.first_name)

    # query = select(User).where(User.first_name.icontains('ali'))
    # print(query)
    # for user in session.scalars(query):
    #     print(user.id, user.first_name, user.last_name, user.phone)

    # query = select(User.phone, User.id, User.first_name, User.last_name).where(User.first_name.icontains('ali'))
    # print(query)
    # print(session.scalar(query))
    # for user in session.scalars(query):
    #     print(user.id, user.first_name, user.last_name, user.phone)


    # while True:
    #     menu = """
    #     10. kursdan kursga otish
    #     """
    #     key = input(menu)
    #     if key == "10":
    #         query = select(User).order_by(User.id.desc())
    #         students = session.scalars(query)
    #         for student in students:
    #             print(student)
    #
    #         _id = input("Studentni tanlang! (id sini kiriting)")
    #
    #         query = select(User).filter(User.id == _id)
    #         student = session.scalar(query)
    #         print(f"{student.first_name} ning kurslari: ")
    #         for course in student.courses:
    #             print(f"{course.id} - {course.name}")
    #         old_course_id = input("Kursni tanlang: ")
    #
    #         # check_course = any(course.id == old_course_id for course in student.courses)
    #         query = select(User).filter(User.courses.any(Course.id == old_course_id), User.id == student.id)
    #         check_course_query = list(session.scalars(query))
    #
    #         if not check_course_query:
    #             print(f"{student.first_name} {old_course_id} idli kursda oqimaydi!")
    #             continue
    #
    #         new_course_id = input("Yangi kursni tanlang: ")
    #         query = select(Course).filter(Course.id == new_course_id)
    #         new_course = session.scalar(query)
    #         if new_course is None:
    #             print("Bunday kurs yoq")
    #             continue
    #
    #         query = update(user_courses).values(course_id=new_course.id).where(
    #             user_courses.c.student_id == student.id,
    #             user_courses.c.course_id == old_course_id
    #         )
    #
    #         # query = update(user_courses).values(course_id=new_course.id).where(Course.id==old_course_id, User.id==student.id)
    #
    #         session.execute(query)
    #         session.commit()

"""
Homework
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
