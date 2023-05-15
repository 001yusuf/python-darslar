# def tugulganyil():
#     ism = str(input("Ismingizni kiriting: "))
#     yosh = int(input("Yoshingizni kiriting: "))
#     x = 2023
#     print("Salom: ", ism, "Yoshingiz: ", x-yosh)
    

# tugulganyil()




# def raqam():
#     raqam = int(input("Istalgan raqamni kiriting: "))
#     print(raqam**2, raqam**3)
# raqam()


# def raqam():
#     raqam = int(input("Istalgan raqamni kiriting: "))
#     if raqam % 2 == 0:
#         print("Raqamingiz juft")
#     else:
#         print("Raqamingiz tog")
# raqam()


# def raqam():
#     raqam = int(input("Istalgan raqamni kiriting: "))
#     raqam2 = int(input("Istalgan raqamni kiriting: "))


# def higest_even(li):
#     evens= []
#     for item in li:
#         if item % 2== 0:
#             evens.append(item)
#     return max(evens)
# print(higest_even([10,2,3,4,8,11]))

# ism=input("Ismingizni kriting: ")
# familiya=input("Familiyangizni kriting: ")
# yosh=input("Tug'ilgan yilingizni kriting: ")
# manzil=input("Manzilingizni kriting: ")
# raqam=input("Telefon raqamingizni kriting: ")

# def malumotlar():
#     print(input("Ismingizni kriting: "))
#     print(input("Familiyangizni kriting: "))
#     print(input("Tug'ilgan yilingizni kriting: "))
#     print(input("Tug'ilgan yilingizni kriting: "))
# malumotlar()


# def katta(soz):
#     return soz.upper

# import math
# print(math.sqrt(13689))

# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar

# ismlar = ['botir', 'bobir', 'aziz', 'murodil']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)


# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)

# print(summa(4,5,6,7))

# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
# print(summa(2))

# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
# print(avto2)
# import math

# def kopaytma(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return math.prod(sonlar)
# print(kopaytma(4,5,6,7))


# def talaba_info(ism, familiya, **boshqa_malumotlar):
#     boshqa_malumotlar['ism'] = ism
#     boshqa_malumotlar['familiya'] = familiya
#     return boshqa_malumotlar

# talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT') 


# filename = 'data/talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)

# faylnomi = 'ustozlar.txt'# ochilayotgan (yaratilayotgan) fayl nomi
# with open(faylnomi,'w') as fayl:
#     fayl.write('anvar narzullaev') # faylga yozilayotgan ma'lumot