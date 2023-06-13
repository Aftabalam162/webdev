from django import forms
from .models import Librarian, Book, Member, BookIssue, Transaction

class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['name', 'phone', 'address', 'username', 'password']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'isbn', 'num_of_copies']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_id', 'name', 'phone', 'membership_status', 'books_issued', 'fine_amount']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['isbn', 'memberId', 'issuedDate', 'dueDate']

class BookIssueForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ['isbn', 'member_id', 'returned_date', 'comments']
