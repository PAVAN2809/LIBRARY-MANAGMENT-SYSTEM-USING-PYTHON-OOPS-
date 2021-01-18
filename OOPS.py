
class Libray():

    def __init__(self,list,name):
        self.name = name
        self.booklist = list
        self.lendic = {}

    def display(self):
        print("We have the following books in {}".format(self.name))
        for books in self.booklist:
            print(books)

    def lendBook(self,user,book):
        if book not in self.lendic.keys():
            self.lendic.update({book : user})
            print("Lender book database has been updated")
        else:
            print("{} has the following {}".format(self.lendic[book],book))

    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added to the library")

    def returnBook(self,book):
        self.lendic.pop(book)

if __name__ == '__main__':

    harry = Libray(['PYTHON','C++','JAVA','C FUNDAMENTALS'],"BML LIBRARY")

    while(True):
        print("Welcome to {} library ".format(harry.name))
        print("1.Display books")
        print("2.lend book")
        print("3.add book")
        print("4.return book")

        userchoice = int(input())

        if userchoice==1:
            harry.display()

        elif userchoice==2:
            user = input("ENTER UR NAME")
            book = input("enter the name of the book")
            harry.lendbook(user,book)

        elif userchoice==3:
            book = input("Enter the name of the book you want to add:")
            harry.addBook(book)

        elif userchoice == 4:
            book = input("Enter the name of the book you want to return:")
            harry.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue