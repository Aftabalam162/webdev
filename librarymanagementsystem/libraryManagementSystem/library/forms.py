from django import forms
from django.core.exceptions import ValidationError
from .models import Librarian, Book, Member, BookIssue, Transaction

class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['name', 'phone', 'address', 'username', 'password']

    labels = {
        'name': 'Name',
        'phone': 'Contact',
        'address': 'Address',
        'username': 'Username',
        'password': 'Password'
    }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'isbn', 'num_of_copies']

    label = {
        'title': 'Title',
        'author': 'Author',
        'publisher': 'Publisher',
        'isbn': 'ISBN',
        'num_of_copies': 'Number of Copies Available'
    }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_id','name', 'phone', 'membership_status', 'books_issued', 'fine_amount']

    label = {
        
    }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['isbn', 'memberId', 'issuedDate', 'dueDate']

    def clean_memberId(self):
        member = self.cleaned_data['memberId']
        if member.membership_status == "Inactive":
            raise ValidationError("Cannot issue book to an inactive member")
        return member

class BookIssueForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ['isbn', 'member_id', 'returned_date', 'comments']
