from models import User, ListUsers
user_1 = User(fullname="Johnny Depp", email="test@test.com",
              password1="password", password2="password")
user_2 = User(fullname="New User", email="user@test.com",
              password1="password", password2="password")

user_list = ListUsers(users=[user_1, user_2])
print(user_list.model_dump())
