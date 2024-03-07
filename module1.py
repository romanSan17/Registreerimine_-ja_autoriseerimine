from sre_constants import ANY


def registreerimine(l:list ,p:list,n=1)->any:
    """funktsioon registreerib kasutaja
    param str l:login
    param str p:pasword
    :param int n: inimeste arv
    """

    if n>0:
        for j in range(n):
            user=True
            while user:
                new_user = input("login: ")
                if new_user not in l:
                    user = False
                else:
                    print("error")
            l.append(new_user)
            p.append(psw)
    return l,p

def autoriseerimine(l:str, p:str)->any:
    users_check=("Sisestage kasutajanimi valideerimiseks: ")
    if users_check in users:
        print("Kasutaja leitud")
    else:
        print("registreerimiseks vajutage 1")
