from django.urls import path
from .views.views import Book, Member, BookIssue, Transaction
from .views.customViews import Success, UpdateBook, UpdateBookIssue, UpdateMember, UpdateTransaction, RemoveBook, RemoveMember, IssueBook, ListMember


urlpatterns = [
    path("", Success.as_view(), name="Index"),
    path("addbook/", Book.as_view(), name="addBook"),
    path("addmember/", Member.as_view(), name="addMember"),
    path("addreturnentry/", BookIssue.as_view(), name="addReturnEntry"),
    path("addtransaction/", Transaction.as_view(), name="addTransaction"),
    path("success/", Success.as_view(), name="success_url"),
    path("updatebook/", UpdateBook.as_view(), name="updateBook"),
    path("updatemember/", UpdateMember.as_view(), name="updateMember"),
    path("updatereturnentry/", UpdateBookIssue.as_view(), name="updateReturnEntry"),
    path("updatetransaction/", UpdateTransaction.as_view(), name="updateTransaction"),
    path("removebook/", RemoveBook.as_view(), name="removeBook"),
    path("removemember/", RemoveMember.as_view(), name="removeMember"),
    path("issuebook/", IssueBook.as_view(), name="issueBook"),
    path("listmember/", ListMember.as_view(), name="listMember"),
]