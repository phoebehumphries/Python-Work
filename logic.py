from main import Closing_File, print_people, create_person

def menu():

    menu = True
    while menu:
        print("Welcome to the menu!")
        print("Please select one of the following:")
        print("1 - Create a new profile")
        print("2 - Print the profile list")
        print("3 - Exit the menu")

        menu = input("What do you want to do?")
        if menu == '2':
          print()
          print_people()
          Closing_File()
          print()

        elif menu == '1':
          print()
          create_person()
          Closing_File()
          print_people()
          print()

        elif menu == '3':
          print()
          print("Saving...")
          print("Goodbye for now.")
          Closing_File()
          exit()


if __name__ == '__main__':
    menu()
