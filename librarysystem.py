class Person:
    def __init__(self,name):
        self.name=name

class Book(Person):
    def __init__(self, name,Book_id,tittle,aurther,__quantity):
        super().__init__(name)
        self.Book_id=Book_id
        self.tittle=tittle
        self.aurther=aurther
        self.__quantity=__quantity

    def display(self):
        try:
         print(f"Name:{self.name}\nBook_id:{self.Book_id}\nTittle:{self.tittle}\nAurther:{self.aurther}\nQuantity:{self.__quantity}\n")
        except ValueError:
           print("Name: must be valid,id must be integer,tittle and aurther must be valid and quantity must bigger than 0: ")
    def get_quantity(self):
        self.get_quantity
        return
    def set_quantity(self,quantity):
        if quantity>0:
            self.__quantity=quantity
        else:
            print("Invalid quantity:")

class Manager:
    def __init__(self):
      self.student=[]
    def Add(self):
     try:
       name=str(input("Enter a name:"))
       id=int(input("Enter a Book_id:"))
       tittle=str(input("Enter a tittle:"))
       aurther=str(input("Enter a aurther:"))
       quantity=int(input("Enter a quantity:"))
       book=Book(name,id,tittle,aurther,quantity)
       self.student.append(book)
       return print("ADDED SUCCESSFULLY")
     except ValueError:
           print("Name: must be valid,id must be integer,tittle and aurther must be valid and quantity must bigger than 0: ")
        

    def View(self):
          for book in self.student:
              book.display()

    def Search(self,tittle):
        try:
         tittle=str(input("Enter a tittle:"))
         for book in self.student:
            if book.tittle==tittle:
                book.display()
                return
        except ValueError:
           print("Tittle must be valid:")

    def Update(self,tittle):
        try:
         tittle=str(input("Enter a tittle:"))
         for book in self.student:
            if book.tittle==tittle:
             book.name=str(input("Enter a name:"))
             book.id=int(input("Enter a Book_id:"))
             book.tittle_1=str(input("Enter a tittle:"))
             book.aurther=str(input("Enter a aurther:"))
             book.quantity=int(input("Enter a quantity:"))
             return
            print("tittle not found:")
        except ValueError:
           print("Tittle must be valid:")



    def delete(self,tittle):
        try:
         tittle=str(input("Enter a tittle:"))
         for book in self.student:
            if book.tittle==tittle:
                self.student.remove(book)
                return
            print("NOT DELETED:")
        except ValueError:
           print("Tittle must be a valid:")


m=Manager()

while True:
 print("\n\t\t\t\t\tLIBRARY MANAGEMENT SYSTEM:")
 print("1.ADD")
 print("2.VIEW")
 print("3.SEARCH")
 print("4.UPDATE")
 print("5.DELETE")
 print("6.EXIT")
 choice=int(input("Enter a choice:"))
 if choice==1:
    m.Add()
 elif choice==2:
    m.View()
 elif choice==3:
    m.Search("tittle")
 elif choice==4:
    m.Update("tittle")
 elif choice==5:
    m.delete("tittle")
 elif choice==6:
  print("EXIT PROGRAM:")  
  break
 


 