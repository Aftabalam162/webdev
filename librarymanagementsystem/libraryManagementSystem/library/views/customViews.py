from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from ..forms import BookForm, MemberForm, BookIssueForm, TransactionForm, RemoveBookForm, RemoveMemberForm
from .views import FormView
from ..models import Book, BookIssue, Member, Transaction


class Success(FormView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
   
    
class UpdateFormView(FormView):
    form_class = None
    template_name = None
    object = None
    identifier = None

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            # getting the object
            object = self.object.objects.get(**{self.identifier: cleaned_data[self.identifier]})
            
            for field in cleaned_data:
                if cleaned_data[field]:
                    setattr(object, field, cleaned_data[field])

            object.save()
            return HttpResponseRedirect("success/")
        return render(request, self.template_name, {"form": form})
        
class UpdateBook(UpdateFormView):
    form_class = BookForm
    template_name = "updatebook.html"
    object = Book
    identifier = "isbn"

class UpdateMember(UpdateFormView):
    form_class = MemberForm
    template_name = "updatemember.html"
    object = Member
    identifier = "member_id"

class UpdateBookIssue(UpdateFormView):
    form_class = BookIssueForm
    template_name = "updatebookissue.html"
    object = BookIssue
    identifier = "bookreturn_id"

class UpdateTransaction(UpdateFormView):
    form_class = TransactionForm
    template_name = "updatetransaction.html"
    object = Transaction
    identifier = "transaction_id"

class RemoveFormView(FormView):
    form_class = None
    template_name = None
    object = None
    identifier = None

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            identifier = cleaned_data[self.identifier]

            object = self.object.objects.get(Q(id=identifier) | Q(title=identifier))

            object.delete()

            return HttpResponseRedirect("success/")
        return render(request, self.template_name, {"form": form})

class RemoveBook(RemoveFormView):
    form_class = RemoveBookForm
    template_name = "deletebook.html"
    object = Book
    identifier = "title"

class RemoveMember(RemoveFormView):
    form_class = RemoveMemberForm
    template_name = "deletemember.html"
    object = Member
    identifier = "member_id"

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            identifier = cleaned_data[self.identifier]

            object = self.object.objects.get(member_id = identifier)

            object.delete()

            return HttpResponseRedirect("success/")
        return render(request, self.template_name, {"form": form})

class IssueBook(FormView):
    form_class = TransactionForm
    template_name = "issuebook.html"


class ListMember(FormView):
    members = Member.objects.all()
    template_name = "memberslist.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"members": self.members})

