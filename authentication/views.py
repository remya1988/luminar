
from authentication.models import users

def authenticate(**kwargs):
    uname = kwargs.get("username")
    passw = kwargs.get("password")
    user = [user for user in users if user["username"]==uname and user["password"] == passw ]
    print(user)
authenticate(username="django",password="django@123")
