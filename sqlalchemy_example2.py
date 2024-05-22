from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(nullable=False)
    email_address:Mapped[str]
    comments:Mapped[List["Comment"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"<User name={self.username}>"


class Comment(Base):
    __tablename__ = "comments"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    text:Mapped[str] = mapped_column(Text, nullable=False)
    user:Mapped["User"] = relationship(back_populates="comments")

    def __repr__(self) -> str:
        return f"<Comment ={self.text}> by {self.user.username}"

if __name__ == "__main__":
    engine = create_engine("sqlite:///sample.db")
    with engine.connect() as connection:
        session = Session(bind=engine)
        # user1 = User(username="nikita", email_address="vatraltd@gmail.com",
        #              comments=[Comment(text="Text"), Comment(text="text2")])
        # session.add(user1)
        # session.commit()
        # Base.metadata.create_all(bind=engine)

        # one way  to filter out
        # statement = select(User).where(User.username.in_(["nikita", "romio"]))
        statement = select(User).where(User.username=="Changed name")
        result = session.scalars(statement)
        all_users = result.fetchall()
        for user in all_users:
            user.comments.append(Comment(text="New comment"))
        session.commit()
        print(all_users)
        # del all_users[0]
        # all_users[0].username = "Changed name"
        # session.delete(all_users[4])
        # session.commit()

        # other way
        # filter_users = session.query(User).filter_by(
        #     username = "nikita"
        # )
        # print(filter_users.first())

        # statement = select(User).join(User.comments).where(
        #     User.username == "nikita"
        # ).where(Comment.text == "Text")
        # print(session.scalars(statement).fetchall())

        # comment = session.query(Comment).filter_by(text="Text_updated").first()
        # comment.text = "Text_updated"
        # session.commit()

        #inserting
        # test_user = User(username="User1", email_address="user1@gmail.com")
        # session.add(test_user)
        # session.commit()

        # print(comment)