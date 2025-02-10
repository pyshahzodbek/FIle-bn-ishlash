import pickle
talaba1={'ism':"Shahzod","familya":"Ravshanov",'tyil':2006,'kurs':1}
talaba2={'ism':"Otabek","familya":"Islomov",'tyil':2005,'kurs':2}

with open('info','wb') as fayl:
    pickle.dump(talaba1,fayl)
    pickle.dump(talaba2,fayl)
with open('info','rb') as fayl:
    talaba1=pickle.load(fayl)
    talaba2=pickle.load(fayl)
print(talaba1)
print(talaba2)