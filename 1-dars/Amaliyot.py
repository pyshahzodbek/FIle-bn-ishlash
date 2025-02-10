"""
Amaliyot
"""

faynomi='Amaliyot.txt'

with open(faynomi,'w')  as fayl:
    fayl.write(f" Ushbu bo'limda katta hajmdagi ma'lumotlarni"
               f" fayldan yuklab olish va dastur yakunida kerakli ma'lumotlarni va"
               f" dastur natijasini faylga saqlashni o'rganamiz. Fayllar bilan ishlash dastur "
               f"foydalanuvchilariga ham dasturga o'zlari istagan ma'lumotlarni yuklash imkoniyatini beradi.")


with open('pi_million_digits.txt') as fayl:
    pi=fayl.read()
    pi=pi.rstrip()
    pi=pi.replace('\n','')
    pi=pi.replace(' ','')
    # pi=float(pi)
print(pi)
tyil='20061409'
print(tyil in pi)
import pickle
with open('pi.pickle','wb') as fayl:
    pi=float(pi)
    pickle.dump(pi,fayl)
with open('pi.pickle','rb') as fayl:
    pi=pickle.load(fayl)
print(pi)

with open('file.txt','a+') as fayl:
    fayl.write(input(f"Ma'lumotlaringizni kiriting: "))
