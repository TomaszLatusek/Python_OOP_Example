from users import *
from Teacher import *
from Student import *
from Course import *
from Grade import *

x = 1
while(x != 0):
    email = input("Email: ")

    for u in allUsers:
        if(email == u.email):
            user = u

    password = input("Password: ")

    if(password == user.password):
        print("Welcome %s %s" % (user.name, user.lastName))


    user.menu()
    x = input("0 - close    1 - log out\n")

