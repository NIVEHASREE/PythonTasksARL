#import typehints
#print(__name__)

class Books:
    book_rented=[]
    def issue_book(self,person_id,book_id):
        if not self.check_membership(person_id):
            #print("member not found")
            self.display_message("member not found")
            return False
        
        if not self.check_book_exists(book_id) or not self.book_availability(book_id):
            #print("book unavailable")
            self.display_message("book unavailable")
            return False
        
        self.rent_book(person_id,book_id)

    def check_membership(self,person_id):
        return person_id==101
    def check_book_exists(self,book_id):
        return book_id=="B100"
    def book_availability(self,book_id):
        return True
    def rent_book(self,person_id,book_id):
        self.book_rented.append((person_id,book_id))
        #print("Book rented")
        self.display_message("Book rented")

    def display_message(self,message):
        print(message)

books_obj= Books()
books_obj.issue_book(101,"B100")
books_obj.issue_book(102,"B100")



