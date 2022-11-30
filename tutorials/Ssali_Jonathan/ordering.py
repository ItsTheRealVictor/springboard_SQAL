from main import Session, engine, User
from sqlalchemy import desc


local_session = Session(bind=engine)

#ascending order
users_ascending = local_session.query(User).order_by(User.id).all()
for user in users_ascending:
    print(f'User> {user.username} ID> {user.id}')

#descending order
users_descending = local_session.query(User).order_by(desc(User.id)).all()
print(f'User> {user.username} ID> {user.id}')
for user in users_descending:
    pass
