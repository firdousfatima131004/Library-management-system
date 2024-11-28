import pyfiglet
from colorama import init, Fore
from crud import add_book, add_member, get_book, view_member, issue_book, return_book, get_teansaction_by_member, deleteABook

# Initialize colorama
init()

def addNewBook():
     title = input(Fore.GREEN+"Enter book title : ")
     author = input(Fore.GREEN+"Enter book author :")
     isbn = input (Fore.GREEN+"Enter book ISBN no. :")
     count = int(input(Fore.GREEN+"Enter no. of copies : "))
     add_book(title, author, isbn, count)
     print(Fore.GREEN+">New book added !<")
     
def printbook():
     books = get_book()
     for book in books:
          available = "available" if book.count > 0 else "Not Available"
          print(Fore.GREEN+f"{book.id}:  '{book.title}'  by  '{book.author}' - (ISBN no. {book.isbn})  - {available}  ({book.count} copies) ")

def addNewMember():
     name = input(Fore.GREEN+"Enter member name : ")
     email = input(Fore.GREEN+"Enter member email : ")
     add_member(name, email)
     print(Fore.GREEN+">New member added !<")
     
def viewMembers():
     members = view_member()
     for mem in members:
           print(Fore.GREEN+f"{mem.id} : Member name  - {mem.name} , Memeber email  - {mem.email}")

def issueABook():
     book_id = int(input(Fore.GREEN+"Enter book ID: "))
     member_id = int(input(Fore.GREEN+"Enter member ID: "))
     issue_book(book_id, member_id)

def returnABook():
     transaction_id = int(input(Fore.GREEN+"Enter transaction ID: "))
     return_book(transaction_id)

def getTransactionForMember():
     member_id = int(input(Fore.GREEN+"Enter member ID: "))
     transactions = get_teansaction_by_member(member_id)
     for transaction in transactions:
          return_status = "Returned" if transaction.return_date else "Not returned"
          print(f"Transaction ID: {transaction.id} , Book ID: {transaction.book_id} , Issue Date: {transaction.issue_date} , Return Date: {transaction.return_date} , Status: {return_status}")

def deleteBookInStock():
     book_id = int(input("Enter book ID: "))
     deleteABook(book_id)

def main():
    ascii_art = pyfiglet.figlet_format("Welcome to The Library")
    print(Fore.MAGENTA + ascii_art)
    while True:
          print(Fore.WHITE+ "******************************")
          print(Fore.WHITE+"1. Add book")
          print(Fore.WHITE+"2. View book")
          print(Fore.WHITE+"3. Add member")
          print(Fore.WHITE+"4. View member")
          print(Fore.WHITE+"5. Issue book")
          print(Fore.WHITE+"6. Return book")
          print(Fore.WHITE+"7. View transactions by members")
          print(Fore.WHITE+"8. Delete book in stock")
          print(Fore.WHITE+"9. Exit")
          print(Fore.WHITE+"******************************")
          choice = input("Enter your choice : ")
     
          if choice == "1":
               addNewBook()

          elif choice == "2":
               printbook()
          
          elif choice == "3":
               addNewMember()
          
          elif choice == "4":
               viewMembers()
     
          elif choice == "5":
               issueABook()
     
          elif choice == "6":
               returnABook()
     
          elif choice == "7":
               getTransactionForMember()
               
          elif choice == "8":
               deleteBookInStock()
               
          elif choice == "9":
               print(Fore.RED+ "Exited!!!!")
               break
          
          else:
               print(Fore.RED + "You entered wrong value!!")

if __name__ == "__main__":
     main()
