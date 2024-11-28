from database import session
from models import Book , member ,transaction
from datetime import date
from colorama import init, Fore

# Initialize colorama
init()

def add_book(title, author,isbn,count):
     book = Book(title = title, author =author ,isbn = isbn , count=count)
     session.add(book)
     session.commit()
     
def get_book():
     return session.query(Book).all()
     
def add_member(name, email):
     members = member(name = name , email = email)
     session.add(members)
     session.commit()
     
def view_member():
     return session.query(member).all()

def issue_book(book_id ,member_id):
     book = session.query(Book).filter_by(id = book_id).first()
     if book and book.count > 0:
          transactions = transaction(book_id = book_id , member_id =member_id ,issue_date = date.today())
          
          book.count -=1
          session.add(transactions)
          session.commit()
          print(Fore.GREEN+">Book is issued.")
     
     else:
          print(Fore.RED+">Book is not available for issue")
     
def return_book(transaction_id):
     transactions = session.query(transaction).filter_by(id = transaction_id).first()
     if transactions and not transactions.return_date:
          transactions.return_date = date.today()
          book = session.query(Book).filter_by(id = transaction.book_id).first()
          book.count +=1
          session.commit()
          print(Fore.GREEN+">Book is returned to library")
          
     else:
          print(Fore.RED+">Book already returned")
          
def get_teansaction_by_member(member_id):
     return session.query(transaction).filter_by(member_id = member_id).all()
          
def deleteABook(book_id):
     book = session.query(Book).filter_by(id = book_id).first()
     if book and book.count >0 :
          book.count = 0
          session.commit()
          print(Fore.GREEN+">Books in stock deleted")
          
     else:
          print(Fore.RED+">Book not in stock")