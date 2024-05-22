from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import Integer, String, Column


class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    #author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    author_id: Mapped[int]

class Tag(Base):
    __tablename__ = "tag"


    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(30))

post_tag = Table(
    "post_tag",
    Base.metadata,
    #Column("author_id", ForeignKey("author.id"), primary_key=True),
    #Column("tag_id", ForeignKey("tag.id"), primary_key=True),
    Column("post_id", Integer, primary_key=True),
    Column("tag_id", Integer, primary_key=True)
)

PWD='Nikita123123'
USR='romio'
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@127.0.0.1:3306/sqlalchemy'.format(USR, PWD)
print(SQLALCHEMY_DATABASE_URI)
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
with engine.connect() as connection:
    # connection.execute(text("CREATE TABLE example(id INTEGER, name VARCHAR(20))"))
    # connection.execute(text("INSERT INTO example (name) VALUES (:name)"), {"name": "Ashley"})
    # connection.execute(text("INSERT INTO example (name) VALUES (:name)"), [{"name": "Barry"}, {"name": "Christina"}])
    # connection.commit()
    result = connection.execute(text("SELECT * from example WHERE name = :name"), dict(name="Ashley"))
    for row in result.mappings():
        print(row["name"])


