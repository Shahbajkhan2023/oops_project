class library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBook(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lneder-Book database has been update. You can tak ethe book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    shahbaj = library(['Python', 'Rich Daddy Poor Daddy', 'Harry Porter'], "Codewithshahbaj")

    while(True):
        print(f"Welcome to the {shahbaj.name} Library . Enter your choice to continue.")
        print("1. Display Books ")
        print("2. Lend a Books ")
        print("3. Add a Books ")
        print("4. Return Books ")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option ")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            shahbaj.displayBook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input('Enter your name: ')
            shahbaj.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            shahbaj.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            shahbaj.returnBook(book)

        print('Press q to quit and c to continue: ')
        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 != 'q'):
            user_choice2 = input()
            if user_choice2 not in ['q', 'c']:
                print('Please enter Q for quit or C for continue:')
                continue
            if user_choice2 == 'q':
                exit()
            elif user_choice2 == 'c':
                continue
