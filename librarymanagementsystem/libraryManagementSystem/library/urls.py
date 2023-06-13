from django.urls import path
from .views import LibrarianForm, BookForm, MemberForm, BookIssueForm, TransactionForm


urlpatterns = [
    path("addlibrarian/", LibrarianForm.as_view(), name="addLibrarian"),
    path("addbook/", BookForm.as_view(), name="addBook"),
    path("addMember/", MemberForm.as_view(), name="addMember"),
    path("addReturnEntry/", BookIssueForm.as_view(), name="addReturnEntry"),
    path("addTransaction/", TransactionForm.as_view(), name="addTransaction"),
]