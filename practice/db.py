from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Create a base class
Base = declarative_base()

# Define User table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', created_at='{self.created_at}')>"

# Define Post table
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationships
    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")

    def __repr__(self):
        return f"<Post(title='{self.title}', content='{self.content}', created_at='{self.created_at}')>"

# Define Comment table
class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    content = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    # Relationships
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")

    def __repr__(self):
        return f"<Comment(content='{self.content}', created_at='{self.created_at}')>"

# Define additional tables as needed...

# Create an engine and connect to a database (Update the connection string)
engine = create_engine('sqlite:///example.db', echo=True)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example usage - creating and adding new users, posts, and comments
new_user = User(username='johndoe', email='johndoe@example.com')
session.add(new_user)

new_post = Post(title='Hello World', content='This is my first post!', user=new_user)
session.add(new_post)

new_comment = Comment(content='Nice post!', user=new_user, post=new_post)
session.add(new_comment)

session.commit()

# Querying data
users = session.query(User).all()
for user in users:
    print(user)

posts = session.query(Post).all()
for post in posts:
    print(post)

comments = session.query(Comment).all()
for comment in comments:
    print(comment)

session.close()
