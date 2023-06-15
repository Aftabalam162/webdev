from django.db import models

# Create your models here.

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=255)
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=255)

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

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True, default=0)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    issuedDate = models.DateField()
    dueDate = models.DateField()

    def save(self, *args, **kwargs):
        # Call the parent's save() method
        super().save(*args, **kwargs)

        # Update the member's books_issued field
        member = self.memberId
        book = self.isbn

        if book.title not in member.books_issued:
            if member.books_issued:
                member.books_issued += ', '
            member.books_issued += book.title
            member.save()

            # decreasing the number of copies by one
            book.num_of_copies -= 1
            book.save()

# @receiver(post_save, sender=Transaction)
# def update_books_issued(sender, instance, **kwargs):
#     member = instance.memberId
#     book = instance.isbn.title
#     if book not in member.books_issued:
#         if member.books_issued:
#             member.books_issued += ', '
#         member.books_issued += book
#         member.save()


class BookIssue(models.Model):
    bookreturn_id = models.AutoField(primary_key=True, default=0)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    returned_date = models.DateField()
    comments = models.CharField(max_length=255)
    fine_charged = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)

    def save(self, *args, **krwargs):
        
        super().save()

        member = self.member_id
        bookReturnEntry = self

        if bookReturnEntry.fine_charged:
            member.fine_amount += bookReturnEntry.fine_charged
            member.save()
        
        
        

