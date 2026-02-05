from sqlalchemy import Integer, create_engine
from sqlalchemy.orm import declared_attr, Mapped, DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(cls):
        name = cls.__name__[0].lower()

        for i in cls.__name__[1:]:
            if i.isupper():
                name += '_' + i.lower()
            else:
                name += i

        if name.endswith('y'):
            name = name[:-1] + 'ie'
        return name.lower() + 's'


pg_url = "postgresql://postgres:1@localhost:5432/sqlalchemy_db"

engine = create_engine(pg_url)

