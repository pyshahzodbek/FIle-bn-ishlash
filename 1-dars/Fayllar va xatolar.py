"""
11.02.2025
Mavzu:Fayllar bilan ishlash
"""
with open('pi.txt') as fayl:
       pi= fayl.read()
print(pi)
pi=pi.rstrip()# qator ohiridagi bo'shliqlarni olib tashlaymiz
pi=pi.replace('\n','') # qator tashlash belgisini almashtiramiz
pi=float(pi)
print(pi)
filename='talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)
# with open(filename) as file:
#     talabalar=file.readlines()#Qatorlarni ro'yxat ko'rinishida saqlab olish uchun
# print(talabalar)
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# faylnomi='ustozlar.txt'
# with open(faylnomi,'w') as fayl:
#     fayl.write('Shahzod Ravshanov')

faylnomi='new_file.txt'
ism='Shahzod Ravshanov'
tyil=2006
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')
with open(faylnomi,'a') as fayl:
    fayl.write('Islomov Otabek \n')
    fayl.write('2007')

