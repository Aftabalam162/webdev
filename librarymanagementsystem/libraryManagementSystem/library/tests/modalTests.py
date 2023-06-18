from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Librarian, Book, Member, Transaction, BookIssue

class LibrarianModelTest(TestCase):
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(username='admin', password='admin123')
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)

    def test_create_user(self):
        librarian = Librarian.objects.create_user(username='librarian1', password='lib123', name='John Doe', phone='1234567890', address='Address')
        self.assertEqual(librarian.is_staff, False)
        self.assertEqual(librarian.is_superuser, False)

class TransactionModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Book 1', author='Author 1', publisher='Publisher 1', isbn=1234567890, num_of_copies=5)
        self.member = Member.objects.create(member_id=1, name='Member 1', phone='1234567890', membership_status='Active')

    def test_transaction_creation(self):
        transaction = Transaction.objects.create(isbn=self.book, memberId=self.member, issuedDate='2023-06-01', dueDate='2023-06-15')
        self.assertEqual(transaction.isbn, self.book)
        self.assertEqual(transaction.memberId, self.member)
        self.assertEqual(transaction.issuedDate, '2023-06-01')
        self.assertEqual(transaction.dueDate, '2023-06-15')

class BookIssueModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Book 1', author='Author 1', publisher='Publisher 1', isbn=1234567890, num_of_copies=5)
        self.member = Member.objects.create(member_id=1, name='Member 1', phone='1234567890', membership_status='Active')

    def test_book_issue_creation(self):
        book_issue = BookIssue.objects.create(isbn=self.book, member_id=self.member, returned_date='2023-06-15', comments='Returned')
        self.assertEqual(book_issue.isbn, self.book)
        self.assertEqual(book_issue.member_id, self.member)
        self.assertEqual(book_issue.returned_date, '2023-06-15')
        self.assertEqual(book_issue.comments, 'Returned')

class MemberModelTest(TestCase):
    def test_member_creation(self):
        member = Member.objects.create(member_id=1, name='Member 1', phone='1234567890', membership_status='Active')
        self.assertEqual(member.member_id, 1)
        self.assertEqual(member.name, 'Member 1')
        self.assertEqual(member.phone, '1234567890')
        self.assertEqual(member.membership_status, 'Active')

class BookModelTest(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(title='Book 1', author='Author 1', publisher='Publisher 1', isbn=1234567890, num_of_copies=5)
        self.assertEqual(book.title, 'Book 1')
        self.assertEqual(book.author, 'Author 1')
        self.assertEqual(book.publisher, 'Publisher 1')
        self.assertEqual(book.isbn, 1234567890)
        self.assertEqual(book.num_of_copies, 5)
