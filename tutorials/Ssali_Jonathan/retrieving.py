from main import User, Session, engine

local_session = Session(bind=engine)

# users = local_session.query(User).all()[:3]
for user in users:
    print(user.username)

# query for a single object
dudu = local_session.query(User).filter(User.username=='dudu').first()
print(dudu)