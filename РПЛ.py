import colorama as color
from colorama import Fore,Back,Style
import random as rdm
import time as tm
import sys

Zenit=1890
Lokomotiv=1800
Krasnodar=1760
CSKA=1740
Rostov=1700
Dinamo=1650
Arsenal=1600
Ufa=1600
Spartak=1580
Rubin=1560
Yral=1560
Sochi=1520

print("Вот возможные команды:"+Back.CYAN+Fore.WHITE+"Зенит "+Back.GREEN+Fore.RED+"Локомотив "+Fore.BLACK+"Краснодар "+Back.BLUE+Fore.WHITE+"ЦС"+Back.RED+"КА"+Style.RESET_ALL)
print("                      "+Back.YELLOW+Fore.BLUE+"Ростов "+Back.BLUE+Fore.WHITE+"Динамо "+Back.RED+"Арсенал "+Fore.YELLOW+"Уфа "+Style.RESET_ALL)
print("                      "+Back.RED+Fore.WHITE+"Спартак "+Back.MAGENTA+"Рубин "+Back.BLACK+Fore.YELLOW+"Урал "+Back.WHITE+Fore.BLUE+"Сочи"+Style.RESET_ALL)
v_team1=input("Выбери первую команду:\n\t")
v_team2=input("Выбери вторую команду:\n\t")

try:
    v_speed=int(input("Выбери ускорение(желательно 90 и более)\tx"))
    speed=1/v_speed
except ValueError:
    print("надо было выбрать цыфру, перезапускай:(")
    sys.exit()

if v_team1.lower()=="зенит":
    team1=Zenit
    tm1=(Back.CYAN+Fore.WHITE+"Зенит"+Style.RESET_ALL)
elif v_team1.lower()=="краснодар":
    team1=Krasnodar
    tm1=(Fore.BLACK+Back.GREEN+"Краснодар"+Style.RESET_ALL)
elif v_team1.lower()=="локомотив":
    team1=Lokomotiv
    tm1=(Back.GREEN+Fore.RED+"Локомотив"+Style.RESET_ALL)
elif v_team1.lower()=="спартак":
    team1=Spartak
    tm1=(Fore.WHITE+Back.RED+"Спартак"+Style.RESET_ALL)
elif v_team1.lower()=="сочи":
    team1=Sochi
    tm1=(Back.WHITE+Fore.BLUE+"Сочи"+Style.RESET_ALL)
elif v_team1.lower()=="цска":
    team1=CSKA
    tm1=(Back.BLUE+Fore.WHITE+"ЦС"+Back.RED+"КА"+Style.RESET_ALL)
elif v_team1.lower()=="ростов":
    team1=Rostov
    tm1=(Back.YELLOW+Fore.BLUE+"Ростов"+Style.RESET_ALL)
elif v_team1.lower()=="динамо":
    team1=Dinamo
    tm1=(Back.BLUE+Fore.WHITE+"Динамо"+Style.RESET_ALL)
elif v_team1.lower()=="арсенал":
    team1=Arsenal
    tm1=(Fore.WHITE+Back.RED+"Арсенал"+Style.RESET_ALL)
elif v_team1.lower()=="уфа":
    team1=Ufa
    tm1=(Back.RED,Fore.YELLOW+"Уфа"+Style.RESET_ALL)
elif v_team1.lower()=="рубин":
    team1=Rubin
    tm1=(Back.MAGENTA+Fore.WHITE+"Рубин"+Style.RESET_ALL)
elif v_team1.lower()=="урал":
    team1=Yral
    tm1=(Back.BLACK+Fore.YELLOW+"Урал"+Style.RESET_ALL)
else:
    print(v_team1,"нету в выборе команд...")
    sys.exit()
if v_team2.lower()=="зенит":
    team2=Zenit
    tm2=(Back.CYAN+Fore.WHITE+"Зенит"+Style.RESET_ALL)
elif v_team2.lower()=="краснодар":
    team2=Krasnodar
    tm2=(Fore.BLACK+Back.GREEN+"Краснодар"+Style.RESET_ALL)
elif v_team2.lower()=="локомотив":
    team2=Lokomotiv
    tm2=(Back.GREEN+Fore.RED+"Локомотив"+Style.RESET_ALL)
elif v_team2.lower()=="спартак":
    team2=Spartak
    tm2=(Fore.WHITE+Back.RED+"Спартак"+Style.RESET_ALL)
elif v_team2.lower()=="сочи":
    team2=Sochi
    tm2=(Back.WHITE+Fore.BLUE+"Сочи"+Style.RESET_ALL)
elif v_team2.lower()=="цска":
    team2=CSKA
    tm2=(Back.BLUE+Fore.WHITE+"ЦС"+Back.RED+"КА"+Style.RESET_ALL)
elif v_team2.lower()=="ростов":
    team2=Rostov
    tm2=(Back.YELLOW+Fore.BLUE+"Ростов"+Style.RESET_ALL)
elif v_team1.lower()=="динамо":
    team2=Dinamo
    tm2=(Back.BLUE+Fore.WHITE+"Динамо"+Style.RESET_ALL)
elif v_team2.lower()=="арсенал":
    team2=Arsenal
    tm2=(Fore.WHITE+Back.RED+"Арсенал"+Style.RESET_ALL)
elif v_team2.lower()=="уфа":
    team2=Ufa
    tm2=(Back.RED,Fore.YELLOW+"Уфа"+Style.RESET_ALL)
elif v_team2.lower()=="рубин":
    team2=Rubin
    tm2=(Back.MAGENTA+Fore.WHITE+"Рубин"+Style.RESET_ALL)
elif v_team2.lower()=="урал":
    team2=Yral
    tm2=(Back.BLACK+Fore.YELLOW+"Урал"+Style.RESET_ALL)
else:
    print(v_team1,"нету в выборе команд...")
    sys.exit()

min=0
sec=0
st1=0
st2=0

r1=rdm.randint(0,int(team2))
r2=rdm.randint(0,int(team1))

print(tm1,Style.BRIGHT+str(st1),":",str(st2)+Style.RESET_ALL,tm2)

while min!=45:
    while sec!=60:
        sys.stdout.write(str(min)+":"+str(sec)+'\r')
        tm.sleep(speed)
        sec+=1
        if r1==0:
            st1+=1
            print("\n"+tm1+str(min)+":"+str(sec))
            r1=rdm.randint(0,int(team2))
        elif r1!=0:
            r1=rdm.randint(0,int(team2))
        if r2==0:
            st2+=1
            print("\n"+tm2+str(min)+":"+str(sec))
            r2=rdm.randint(0,int(team1))
        elif r2!=0:
            r2=rdm.randint(0,int(team1))
    sec=0
    min+=1
print("\n"+tm1,Style.BRIGHT+str(st1),":",str(st2)+Style.RESET_ALL,tm2)
sys.stdout.write("1тайм\r")
tm.sleep(3)
while min!=90:
    while sec!=60:
        sys.stdout.write(str(min)+":"+str(sec)+'\r')
        tm.sleep(speed)
        sec+=1
        if r1==0:
            st1+=1
            print("\n"+tm1+str(min)+":"+str(sec))
            r1=rdm.randint(0,int(team2))
        elif r1!=0:
            r1=rdm.randint(0,int(team2))
        if r2==0:
            st2+=1
            print("\n"+tm2+str(min)+":"+str(sec))
            r2=rdm.randint(0,int(team1))
        elif r2!=0:
            r2=rdm.randint(0,int(team1))
    sec=0
    min+=1
print("\n"+tm1,Style.BRIGHT+str(st1),":",str(st2)+Style.RESET_ALL,tm2)
if st1>st2:
    print(tm1,"побеждает!")
elif st2>st1:
    print(tm2,"побеждает!")
else:
    print("Ничья!")