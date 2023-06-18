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

        labels = {
            'title': 'Title',
            'author': 'Author',
            'publisher': 'Publisher',
            'isbn': 'ISBN',
            'num_of_copies': 'Copies Available'
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_id','name', 'phone', 'membership_status', 'books_issued', 'fine_amount']

        labels = {
            'member_id': 'MemberID',
            'name': 'Name',
            'phone': 'Phone',
            'membership_status': 'Membership Status',
            'books_issued': 'Books Issued',
            'fine_amount': 'Fine Accrued'
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['isbn', 'memberId', 'issuedDate', 'dueDate', 'returnedDate']

        labels = {
            'isbn': 'ISBN',
            'memberId': 'MemberID',
            'issuedDate': 'Date of Issue',
            'dueDate': 'Due Date',
            'returnedDate': 'Date of Return'
        }

        widgets = {
            'isbn': forms.NumberInput(attrs={'min': 0, 'max': 99999999999999999999}),
            'memberId': forms.NumberInput(attrs={'min': 0, 'max': 999999}),
            'issuedDate': forms.DateInput(attrs={'type': 'date'}),
            'dueDate': forms.DateInput(attrs={'type': 'date'}),
            'returnedDate': forms.DateInput(attrs={'type': 'date'})
        }


    def clean_memberId(self):
        member = self.cleaned_data['memberId']
        if member.membership_status == "Inactive":
            raise ValidationError("Cannot issue book to an inactive member")
        return member

class BookIssueForm(forms.ModelForm):
    # form to fill when a book is being returned
    class Meta:
        model = BookIssue
        fields = ['bookreturn_id','transaction_id', 'isbn', 'member_id', 'returned_date', 'comments', 'fine_charged']

        labels = {
            'bookreturn_id': 'BookReturnID',
            'isbn': 'ISBN',
            'member_id': 'MemberID',
            'returned_date': 'Date of Return',
            'comments': 'Comments',
            'fine_charged': 'Fine Charged',
            'transaction_id': 'TransactionID'
        }

        widgets = {
            'transaction_id': forms.NumberInput(attrs={'min': 0, 'max': 999999}),
            'bookreturn_id': forms.NumberInput(attrs={'min': 0, 'max': 999999}),
            'isbn': forms.NumberInput(attrs={'min': 0, 'max': 99999999999999999999}),
            'member_id': forms.NumberInput(attrs={'min': 0, 'max': 999999}),
            'returned_date': forms.DateInput(attrs={'type': 'date'}),
            'comments': forms.TextInput(),
            'fine_charged': forms.NumberInput()
        }

    def clean_memberId(self):
        member = self.cleaned_data['member_id']
        book = self.cleaned_data['isbn']
        if member.books_issued:
            issuedBooks = member.books_issued.split(', ')
            if book.title == member.books_issued:
                return member
            if book.title in issuedBooks:
                return member
        else: 
            raise ValidationError("No book is issued to this member!")
        return member


