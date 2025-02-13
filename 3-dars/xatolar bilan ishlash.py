"""
14.02.2025
Mavzu:Xatolar bilan ishlash
"""

#try-except
yosh=input("Yoshingizni kiriting: ")
try:
    yosh=int(yosh)
    print(f'Siz {2025-yosh} yilga tug\'ilgansiz.')
except:
    print("Butun son kiriting!")
print("Dastur tugai!")

#try-except-else

yosh=input("Yoshingizni kiriting: ")
try:
    yosh=int(yosh)

except ValueError:
    print("Butun son kiriting!")
else:
    print(f'Siz {2025 - yosh} yilga tug\'ilgansiz.')
print("Dastur tugai!")
#ZeroDivisionError
x,y=5,10
try:
    y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi!")

#IndexError
mavalar=['olma','uzum','anor','anjir']
try:
    print(mavalar[5])
except IndexError:
    print(f" Ro'yxatda {len(mavalar)}ta meva bor xolos")

#KeyError
user={
     "username":'sariqdev',
     "status":"admin",
     "email":"admin@sariq.dev",
     "phine":"99897123456"
 }
key="tel"
try:
     print(f"Foydalanuvchi: {user[key]}")
except KeyError:
    print(f"Bunday kalit mavjud emas!")
# FileNotFoundError

filname="data.txt" # bunday fayl mavjud emas
try:
    with open(filname) as f:
        text=f.read()
except FileNotFoundError:
    print("Fayl mavjud emas!")
# BIR NECHTA XATOLARNI USHLASH
n=input("Butun som kiriting: ")
try:
    n=int(n)
    x=20/n
except ValueError:
    print("Butun son kiriting!")
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi!")
else:
    print(f'x={x}')
print("Dastur tugai!")

#ATOLARNI KO'RSATMAY O'TISH
import  json
files=['talaba1.json',"talaba2.json","talaba3.json","talaba4.json"]
for filename in files:
    try:
        with open(filename) as f:
            talaba=json.load(f)
    except FileNotFoundError:
        print(f"{filename} fayl mavjud emas!")
    else:
        print(f"Talaba: {talaba['ism']} {talaba['familiya']}")

# XATOLARNING OLDINI OLISH
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break

print(f"Siz {2021-yosh} yilda tug'ilgansiz")