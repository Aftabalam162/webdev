from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib import messages

# Create your models here.

class LibrarianManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)
    

class Librarian(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=255)
    username = models.CharField(max_length=30, unique=True, primary_key=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone', 'address']

    objects = LibrarianManager()

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    isbn = models.BigIntegerField(primary_key=True)
    num_of_copies = models.IntegerField()

class Member(models.Model):
    MEMBERSHIP_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    member_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    membership_status = models.CharField(max_length=10, choices=MEMBERSHIP_STATUS_CHOICES)
    books_issued = models.CharField(max_length=255, blank=True)
    fine_amount = models.IntegerField(blank=True, default=0, null=True)

# class Transaction(models.Model):
#     transaction_id = models.AutoField(primary_key=True, default=0)
#     isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
#     memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
#     issuedDate = models.DateField()
#     dueDate = models.DateField()
#     returnedDate = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         # Call the parent's save() method
#         super().save(*args, **kwargs)

#         # Update the member's books_issued field
#         member = self.memberId
#         book = self.isbn
#         book_issued = member.books_issued.split(', ')



#         if member.books_issued == book.title:
#             raise ValueError('Cannot issue a book twice to a member!')
#         if book.title in book_issued:
#             raise ValueError('Cannot issue a book twice to a member!')
#         if member.books_issued:
#             member.books_issued += ', '
#         member.books_issued += book.title
#         member.save()
#         # decreasing the number of copies by one
#         book.num_of_copies -= 1
#         book.save()


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    issuedDate = models.DateField()
    dueDate = models.DateField()
    returnedDate = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if the transaction is being created for the first time
        if self.transaction_id is None:
            # Update the member's books_issued field only when creating a new transaction
            member = self.memberId
            book = self.isbn
            book_issued = member.books_issued.split(', ')

            print("Member:", member, ", Book", book)

            if member.books_issued == book.title:
                raise ValueError('Cannot issue a book twice to a member!')
            if book.title in book_issued:
                raise ValueError('Cannot issue a book twice to a member!')
            if member.books_issued:
                member.books_issued += ', '
            member.books_issued += book.title
            member.save()
            # Decrease the number of copies by one
            book.num_of_copies -= 1
            book.save()

        super().save()


 

class BookIssue(models.Model):
    # book returning model form

    bookreturn_id = models.AutoField(primary_key=True)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    returned_date = models.DateField()
    comments = models.CharField(max_length=255, blank=True)
    fine_charged = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def save(self, *args, **krwargs):
        
        bookReturnEntry = self
        book = self.isbn
        member = self.member_id
        transaction = self.transaction_id

        # updating the datefield of the transaction entry
        transaction.returnedDate = bookReturnEntry.returned_date
        transaction.save()
 
        books_issued_list = member.books_issued.split(', ')
        # if it returns none then either no book is issued to the member
        # or a single boook is issued
        if transaction.memberId == self.member_id:
            if transaction.isbn == self.isbn:
                if book.title in books_issued_list:
                    books_issued_list.remove(book.title)
                    member.books_issued = ', '.join(books_issued_list)

                elif book.title == member.books_issued:
                    member.books_issued = ''

                    # remove the book title from member's books_issued field
                else:
                    raise ValueError('No Book is issued to the member')
            else:
                raise ValueError('ISBN entered is incorrect!')
        else:
            raise ValueError('MemberID is incorrect')     

        if bookReturnEntry.fine_charged:
            member.fine_amount += int(bookReturnEntry.fine_charged)

        # charge members fine amount if any
      
        book.num_of_copies += 1

        # increase the copies available by one


        book.save()
        member.save()

        super().save()
        
        
        
        

