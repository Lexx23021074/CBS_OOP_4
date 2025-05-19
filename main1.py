import random
class GoogleUser:
    list_all_users = []

    def __init__(self, email, first_name, second_name):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__email = email
        self.list_all_users.append(self)

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__second_name}'
    
    @property
    def email(self):
        return self.__email
    
    @classmethod
    def find_user(cls, email):
        for user in cls.list_all_users:
            if user.email == email:
                return user
        return None

for i in range(10):
    GoogleUser(f"user{i}@gmail.com", f"User-{i}", f'User-{i}')


class User:
    __list_all_users = []

    def __init__(self, email, password, full_name, is_admin):
        self.__email = email
        self.__password = password
        self.__full_name = full_name
        self.__is_admin = is_admin
        self.__list_all_users.append(self)

    @staticmethod
    def generate_random_password():
        symbols = "qwertyuioasdfghjklzxcvbnm,.[]/^QWERTYUIOPASDFGHJKLZXCVBNM"
        password = ''
        for i in range(random.randint(10,20)):
            if random.randint(0,1):
                password += random.choice(symbols)
            else:
                password += str(random.randint(0,9))
        return password

    @classmethod
    def create_by_google(cls, google_user: GoogleUser):
        new_user = cls(
            email = google_user.email,
            password = cls.generate_random_password(),
            full_name = google_user.full_name,
            is_admin = False
        )
        return new_user
    
    @classmethod
    def get_all_users(cls):
        return cls.__list_all_users

    def __str__(self):
        return f'{self.__email} ({self.__full_name})'
    

while True:
    choice = int(input())
    if choice == 1:
        email = input("Enter email: ")
        full_name = input("Enter full_name: ")
        password = input("Enter password")
        new_user = User(email, password, full_name, True)
    elif choice == 2:
        google_email = input("Enter gmail: ")
        user = GoogleUser.find_user(google_email)
        if user is not None:
            new_user = User.create_by_google(user)
    elif choice == 3:
        for user in User.get_all_users():
            print(user)