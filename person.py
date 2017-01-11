
from datetime import date
from datetime import datetime

class Person:
    '''Define a person'''
#this prints out the doc string^
    
    def __init__(self, firstname, surname, dob, phone):
        '''Assigns instance variables for later use'''
        #the __init__ is the constructor

        self.firstname = firstname
        self.surname = surname
        self.dob = datetime.strptime(dob, '%b %d %Y').date()
        self.age = self.calculate_age(self.dob)
        self.phone = int(phone)


    def calculate_age(self, born):
        '''Calculate age from date of birth'''

        self.__today = date.today()
        self.__years_difference = self.__today.year - born.year
        self.__is_before_birthday = (self.__today.month, self.__today.day) < (born.month, born.day)
        #is the day they are born more than today's date.
        self.__elapsed_years = self.__years_difference - int(self.__is_before_birthday)

        return self.__elapsed_years



