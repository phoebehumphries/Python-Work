from person import Person
import pickle

try:
    with open('personSave.pickle', 'rb')as save:
        people = pickle.load(save)
except FileNotFoundError as errornotsave:
    people = []
    print('File not found:' + str(errornotsave)+ 'When closed, a new file is saved.' )

'''this is a list.'''

def print_people():
    '''Iterates through the people list and prints out details'''
    for person in people:
        print('{0} {1} is {2} years old.'.format(person.firstname, person.surname, person.age))
        print('Phone Number: {0}'.format(person.phone))
        print()
        #the numbers are the order of the different info, so 0 is firstname, 1 is surname e.g.


def create_person():
    ''' User can input their own details '''
    print()
    new_firstname = input("What is your first name? ")
    print()
    new_surname = input("What is your surname? ")
    print()
    new_dob = input("What is your date of birth? Please enter in the form MMM DD YYYY ")
    print()
    new_phone = input("Please enter an 11 digit number:")
    print()
    new_p0 = Person(new_firstname, new_surname, new_dob, new_phone)
    people.append(new_p0)
    return new_p0

def Closing_File():
    '''Write the actual pickle file.'''
    with open('personSave.pickle', 'wb') as save:
        pickle.dump(people, save, protocol=pickle.HIGHEST_PROTOCOL)


#def main():
   # '''Create test users and add them to the people list.'''
   # p1 = Person( 'Phoebe',  'Humphries', 'Sep 15 1999')
    #people.append(p1)
    #p2 = Person('Craig', 'Chambers', 'Jan 21 1968')
    #people.append(p2)
    #p3 = Person('Anju', 'Babu', 'Jan 1 2000')
    #people.append(p3)




