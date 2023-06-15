from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from ..forms import BookForm, MemberForm, BookIssueForm, TransactionForm, RemoveBookForm, RemoveMemberForm
from .views import FormView
from ..models import Book, BookIssue, Member, Transaction
from django.contrib import messages

class Success(FormView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
   
    
class UpdateFormView(FormView):
    # inheriting from FormView so I don't need to define get method
    form_class = None

    model = None
    # name of the form class of which instance I need ex. AddBookForm
    template_name = None
    # name of the object class of which instance I need ex. Book
    identifier = None
    # identifier of the instance ex. ISBN
   

    def post(self, request, *args, **kwargs):

        uniqueId = self.identifier

        pk_value = request.POST.get(self.identifier)
        # this gets us the id of the object

        try:
            my_instance = get_object_or_404(self.model, **{self.identifier: pk_value})
        except Http404:
        # Object not found, handle the error here
            messages.error(request, "Object with primary key not found")
            return render(request, self.template_name, {"form": self.form_class()})
        # this special function returns the exist instance of the model where the identifer = pk_value


        # let say uniqueId = member_id
        # my_instance.uniqueId -> it will search for a "uniqueId" field in "my_instance" object
        # I want it to search for the  my_instance.member_id not my_instance.uniqueId

        uniqueIdValue = getattr(my_instance, self.identifier)

        form = self.form_class(request.POST, instance=my_instance, initial={uniqueId: uniqueIdValue})
        # probably this is creating a new 'Book' object which is not our purpose
    
        if form.is_valid():
            # this gets false if the Form validation fails so you need to make sure the
            # clean() and clean_<field_name>() or any other validation return true (forms.py)
    
            form.save()
            return HttpResponseRedirect(reverse("Index"))
        return render(request, self.template_name, {"form": form})
        
class UpdateBook(UpdateFormView):
    form_class = BookForm
    template_name = "updatebook.html"
    model = Book
    identifier = "isbn"

class UpdateMember(UpdateFormView):
    form_class = MemberForm
    template_name = "updatemember.html"
    model = Member
    identifier = "member_id"

class UpdateBookIssue(UpdateFormView):
    form_class = BookIssueForm
    template_name = "updatebookissue.html"
    model = BookIssue
    identifier = "bookreturn_id"

class UpdateTransaction(UpdateFormView):
    form_class = TransactionForm
    template_name = "updatetransaction.html"
    model = Transaction
    identifier = "transaction_id"

class RemoveFormView(UpdateFormView):
    form_class = None
    template_name = None
    model = None
    identifier = None

    def post(self, request, *args, **kwargs):

        uniqueId = self.identifier

        primarykey_value = request.POST.get(uniqueId)

        my_instance = get_object_or_404(self.model, **{self.identifier: primarykey_value})

        my_instance.delete()
            
        return HttpResponseRedirect(reverse("Index"))

class RemoveBook(RemoveFormView):
    form_class = RemoveBookForm
    template_name = "deletebook.html"
    model = Book
    identifier = "isbn"

class RemoveMember(RemoveFormView):
    form_class = RemoveMemberForm
    template_name = "deletemember.html"
    model = Member
    identifier = "member_id"


class IssueBook(FormView):
    form_class = TransactionForm
    template_name = "issuebook.html"


class ListMember(FormView):
    members = Member.objects.all()
    template_name = "memberslist.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"members": self.members})

class ListBook(FormView):
    books = Book.objects.all()
    template_name = "catalogue.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"books": self.books})

class ListTransaction(FormView):
    transactions = Transaction.objects.order_by('-created_at')[:5]
    template_name = "home.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"transactions": self.transactions})
