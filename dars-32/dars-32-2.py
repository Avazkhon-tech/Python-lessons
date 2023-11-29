"""
Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan 
talabalarning ro'yxati saqlansin. Buning uchun Fanga add_student(),
 __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.
Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing
Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing 
(bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)
Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki fizika(talaba1)). 
Bu metodlarni o'zingiz istagandek talqin qiling.
"""

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
    
    def get_name(self):
        return self.name

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

    def __eq__(self, talaba):
        """obyeklarni bosqichini taqqoslovchi funksiya"""
        return self.bosqich == talaba.bosqich
    def __lt__(self, talaba):
        """obyeklarni bosqichini taqqoslovchi funksiya"""
        return self.bosqich < talaba.bosqich
    def __le__(self, talaba):
        """obyeklarni bosqichini taqqoslovchi funksiya"""
        return self.bosqich <= talaba.bosqich
    
class Fan:
    def __init__(self, fan_nomi):
        self.fan_nomi = fan_nomi
        self.students = []
    
    def __add__(self, y):
        if isinstance(y, Talaba):
            self.add_student(y)
    def __sub__(self, student_id):
        """talabalarni id si buyicha topib uchiradigan funksiya"""
        for student in self.students:
            if student_id == student.get_id():
                self.students.remove(student)
            else:
                print(f"{student_id} id dagi talaba mavjud emas")
    def __call__(self, *qiymatlar):
        if qiymatlar:
            for qiymat in qiymatlar:
                if isinstance(qiymat, Talaba):
                    return qiymat.get_info()
                else: 
                    print('talaba ro\'yxatda mavjud emas')
        else:
            return self.students
            
    def add_student(self, *studentlar):
        """studentlarni royxatga qushuvchi funksiya"""
        for student in studentlar:
            self.students.append(student)
    def remove_student(self, *studentlar):
        for student in studentlar:
            self.students.remove(student)
    def __getitem__(self, index):
        """royxatdagi studentlarni indexi buyicha chaqiruvchi funksiya"""
        return self.students[index]
    def __setitem__(self, index, talaba):
        """royxatdagi studentlarni almastirish uchun funksiya"""
        self.students[index] = talaba
    def __len__(self):
        """royxatdagi studentlar sonini qaytaruvchi funksiya"""
        return len(self.students)
    
    
shaxs1 = Shaxs('ali', 'olimov', 'av244565', 2000)
shaxs2 = Shaxs('Avazkon', 'Nazirov', 'AB1234567', 2001)
talaba1 = Talaba('ali', 'olimov', 'ab123', 2000, 43567)
talaba2 = Talaba('olim', 'aliev', 'sd728', 2000, 43568)
talaba3 = Talaba('sobir', 'husanov', 'to960', 2000, 43569)
talaba4 = Talaba('anvar', 'anvarov', 'jh564', 2005, 34561)
talaba5 = Talaba('temir', 'baxodirov', 'ca546', 2005, 34567)
maths = Fan("matematika")
        