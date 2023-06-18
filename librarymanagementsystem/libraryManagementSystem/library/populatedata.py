import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryManagementSystem.settings')
application = get_wsgi_application()

import django
django.setup()


from faker import Faker
from random import randint
from django.utils import timezone
from datetime import timedelta
from library.models import Book, Member, Transaction, BookIssue

fake = Faker()

def generate_fake_data():
    # Generate fake data for Book model
    for _ in range(50):
        title = fake.catch_phrase()
        author = fake.name()
        publisher = fake.company()
        isbn = fake.unique.random_number(digits=13)
        num_of_copies = randint(1, 10)
        book = Book.objects.create(title=title, author=author, publisher=publisher, isbn=isbn, num_of_copies=num_of_copies)

    # Generate fake data for Member model
    for _ in range(50):
        member_id = fake.unique.random_number(digits=6)
        name = fake.name()
        phone = fake.unique.random_number(digits=10)
        membership_status = fake.random_element(elements=('Active', 'Inactive'))
        books_issued = fake.sentence(nb_words=3)
        fine_amount = randint(0, 100)
        member = Member.objects.create(member_id=member_id, name=name, phone=phone, membership_status=membership_status,
                                       books_issued=books_issued, fine_amount=fine_amount)

    # Generate fake data for Transaction and BookIssue models
    books = Book.objects.all()
    members = Member.objects.all()
    for _ in range(50):
        book = fake.random_element(elements=books)
        member = fake.random_element(elements=members)
        issued_date = fake.date_time_this_decade()
        due_date = issued_date + timedelta(days=7)
        returned_date = fake.date_time_between(start_date=due_date, end_date=timezone.now())
        comments = fake.sentence(nb_words=6)
        fine_charged = fake.pydecimal(left_digits=2, right_digits=2, positive=True)
        transaction = Transaction.objects.create(isbn=book, memberId=member, issuedDate=issued_date, dueDate=due_date, returnedDate=returned_date)
        BookIssue.objects.create(isbn=book, member_id=member, returned_date=returned_date, comments=comments, fine_charged=fine_charged, transaction_id=transaction)

if __name__ == "__main__":
    generate_fake_data()