class library:
    
    def __init__ (self, listOfBooks , libraryName):
        self.listOfBooks = listOfBooks
        self.libraryName = libraryName
        
    def Displaybook(self):
        print("---------Books---------")
        for i in range(len(self.listOfBooks)):
            print(self.listOfBooks[i])
        print("-----------------------")
            
    def Lendbook(self):
        bookName = input("\nEnter book name you want to lend: ")
        try:
            self.listOfBooks.index(bookName)
            self.listOfBooks.remove(bookName)
            self.lended = []
            self.lended.append(bookName)
            print("\nBooks Avialable : " , self.listOfBooks,"\n")
        except:
            print ("Book not found")
            print("\nBooks Avialable : " , self.listOfBooks,"\n")

    def Addbook(self):
        bookName = input("Enter book name: ")
        self.listOfBooks.append(bookName)
        print(self.listOfBooks)

    def Returnbook(self):
        bookName = input("Enter book name: ")
        try:
            self.lended.index(bookName)
            self.lended.remove(bookName)
            self.listOfBooks.append(bookName)
        except:
            print ("Book is not lended")
            print("Books you lended : " , self.lended)
            
    def menu(self):
        print("1- Display Available Books.")
        print("2- lend a book.")
        print("3- Add a book.")
        print("4- Return book.")
        print("5- Exit.")

        x = int(input("Enter option number: "))
        while(x!= 5):
            if x== 1:
                self.Displaybook()
            elif x==2:
                self.Lendbook()
            elif x==3:
                self.Addbook()
            elif x==4:
                self.Returnbook()
            else:
                print("Wrong option number!!!")
            x = int(input("\nEnter Option number: "))
        
books = ["book1","book2","book3"]
lib = library(books, "None")

lib.menu()

