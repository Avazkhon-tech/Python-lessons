# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 19:52:51 2023

@author: Avazkhon
"""

# Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder
# metodlarni qo'shishni mashq qiling.
# Obyekt haqida ma'lumot (__rerp__)
# Talabalarni bosqichi bo'yicha solishtirish (__lt__, __eg__ va hokazo)


class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __shaxs_num = 0

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__user_name = ''
        Shaxs.__shaxs_num += 1
        self.shaxslar_royxati = []
    # 32-dars uchun vazifalar  \starts here\

    def __repr__(self):
        """"Obyekt haqida ma'lumot beradigan funksiya"""
        return f"Talaba: {self.ism} {self.familiya}"

    def yosh_hisobla(self):
        """yosh hisoblovchi funksiya"""
        yosh = 2023-self.tyil
        return yosh

    def __eq__(self, x):
        """obyeklarni yoshi ni taqqoslaydigan funksiya"""
        return self.yosh_hisobla() == x.yosh_hisobla()

    def __lt__(self, x):
        """obyeklarni yoshi ni taqqoslaydigan funksiya"""
        return self.yosh_hisobla() < x.yosh_hisobla()

    def __le__(self, x):
        """obyeklarni yoshi ni taqqoslaydigan funksiya"""
        return self.yosh_hisobla() <= x.yosh_hisobla()
    # 32-dars uchun vazifalar \ends here\

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, username):
        self.__user_name = username

    @classmethod
    def get_shaxslar_soni(cls):
        return cls.__shaxs_num


shaxs1 = Shaxs('ali', 'olimov', 'av244565', 2000)
shaxs2 = Shaxs('Avazkon', 'Nazirov', 'AB1234567', 2001)


class Talaba(Shaxs):
    """Talaba klassi"""
    __Talaba_no = 0

    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.__cars = []
        self.studends_list = []
        Talaba.__Talaba_no += 1

    @classmethod
    def get_talabalar_soni(cls):
        return Talaba.__Talaba_no

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    def add_car(self, car_name):
        self.__cars.append(car_name)

    def remove_car(self, car_name):
        for x in self.__cars:
            if car_name == x:
                self.__cars.remove(x)
            else:
                print("Talabada bundan mashina yo'q")

    def get_cars(self):
        num = 1
        if self.__cars == True:
            for car in self.__cars:
                print(f"{num}. {car}")
                num += 1
        else:
            print("talabada mashina yo'q")

    # 32-dars uchun vazifalar  \starts here\
    def __eq__(self, talaba):
        """obyeklarni bosqichini taqqoslovchi funksiya"""
        return self.bosqich == talaba.bosqich
    def __lt__(self, talaba):
        """obyeklarni bosqichini taqqoslovchi funksiya"""
        return self.bosqich < talaba.bosqich
    def __le__(self, talaba):
        """obyeklarni bosqichini taqqoslovchi funksiya"""
        return self.bosqich <= talaba.bosqich
    # 32-dars uchun vazifalar  \ends here\



class Talabalar:

    def __init__(self, talaba):
        self.talaba = talaba
        self.talabalar_royxati = []

    def get_list(self):
        return self.talabalar_royxati

    def add_students(self, *studentlar):
        for student in studentlar:
            self.talabalar_royxati.append(student)
    # 32-dars uchun vazifalar  \starts here\
    def __str__(self):
        for student in self.talabalar_royxati:
            return student

    def __call__(self, *student):
        if not student:
            return [student for student in self.talabalar_royxati]
        else:
            self.add_students(student)

    def __getitem__(self, index):
        return self.talabalar_royxati[index]
    # 32-dars uchun vazifalar  \ends here\
        
        
        
talaba1 = Talaba('ali', 'olimov', 'ab123', 2000, 43567)
talaba2 = Talaba('olim', 'aliev', 'ab123', 2000, 43567)
talaba3 = Talaba('sobir', 'husanov', 'ab123', 2000, 43567)
talaba4 = Talaba('anvar', 'anvarov', 'ab123', 2005, 34567)
talaba5 = Talaba('anvar', 'anvarov', 'ab123', 2005, 34567)
list1 = Talabalar('Matematika')
list1.add_students(talaba1, talaba2, talaba3, talaba4, talaba5)
