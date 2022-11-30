from main import User, Session, engine

users = [
    {
        "username": "kjsdfjklsdfxcvcvcvcvcvcvcvcvcvcvcv",
        "email": "lzxcvzxcvzxcvzvksldkfjlsdkfj@gflsdkfzxcvjsdlkf.com" 
    },
    {
        "username": "kjsdfvzxcvzxcvzxcvzxjklsdf",
        "email": "lksldkfjlsdkwetwetwetfj@gflserererdkfjsdlkf.com" 
    },
    {
        "username": "kjsdfjklsfdsfdfdf",
        "email": "lksldkfjlwerwetwesdkfj@gflsdkfjsfsdfadlkf.com" 
    },
    {
        "username": "kjsdfjklsdfsdafasdfdf",
        "email": "lksldkffdfdfsdfjlsdkfj@gflsdkfjsdlkf.com" 
    },
]




local_session = Session(bind=engine)


# new_user = User(username='dudu',
#                 email='caca@dudu.com')

# local_session.add(new_user)

# local_session.commit()

for u in users:
    new_user = User(username=u["username"], email=u["email"])
    local_session.add(new_user)
    local_session.commit
