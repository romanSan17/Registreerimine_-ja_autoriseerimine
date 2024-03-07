from module1 import *

users=[]
psw=[]

while True:
    print("0-all_users/n1-registreerimine/n")
    valik=int(input())
    if valik == 1:
        users,psw=registreerimine(users,psw,(input("register?")))
    if valik == 2:
        users=autoriseerimine(users(input("QQQ")))
        