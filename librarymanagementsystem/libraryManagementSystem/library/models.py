from django.db import models

# For post-save actions
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    member_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    membership_status = models.CharField(max_length=10)
    books_issued = models.CharField(max_length=255)
    fine_amount = models.IntegerField()

class Transaction(models.Model):
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    issuedDate = models.DateField()
    dueDate = models.DateField()

@receiver(post_save, sender=Transaction)
def update_books_issued(sender, instance, **kwargs):
    member = instance.memberId
    book = instance.isbn.title
    if book not in member.books_issued:
        if member.books_issued:
            member.books_issued += ', '
        member.books_issued += book
        member.save()


class BookIssue(models.Model):
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    returned_date = models.DateField()
    comments = models.CharField(max_length=255)

