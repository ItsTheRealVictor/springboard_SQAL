from main import Session, engine, User

local_session = Session(bind=engine)

user_to_update = local_session.query(User).filter(User.username=='dudu').first()

user_to_update.username = 'cacaGuy'
user_to_update.email = 'caca@iLoveCaca.com'

local_session.commit