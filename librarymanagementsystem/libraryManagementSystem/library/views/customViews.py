from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from ..forms import BookForm, MemberForm, BookIssueForm, TransactionForm
from .views import FormView
from ..models import Book, BookIssue, Member, Transaction
from django.contrib import messages
from django.core.paginator import Paginator

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
    successtext = None
    # what toast to present if action is performed successfully
   

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
            messages.success(request, self.successtext, extra_tags='success')
            return HttpResponseRedirect(reverse(self.template_name))
        return render(request, self.template_name, {"form": form})
         
class UpdateBook(UpdateFormView):
    form_class = BookForm
    template_name = "updatebook.html"
    model = Book
    identifier = "isbn"
    successtext = "Book details are updated successfully!"

class UpdateMember(UpdateFormView):
    form_class = MemberForm
    template_name = "updatemember.html"
    model = Member
    identifier = "member_id"
    successtext = "Member details are updated successfully!"

class UpdateBookIssue(UpdateFormView):
    form_class = BookIssueForm
    template_name = "updatebookissue.html"
    model = BookIssue
    identifier = "bookreturn_id"
    successtext = "Member details are updated successfully!"

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
    successtext = None

    def post(self, request, *args, **kwargs):

        uniqueId = self.identifier

        primarykey_value = request.POST.get(uniqueId)
        
        try:
            my_instance = get_object_or_404(self.model, **{self.identifier: primarykey_value})
        except Http404:
        # Object not found, handle the error here
            messages.error(request, "Object with primary key not found")
            return render(request, self.template_name, {"form": self.form_class()})        

        my_instance.delete()
        messages.success(request, self.successtext, extra_tags='success')    
        return HttpResponseRedirect(reverse(self.template_name))

class RemoveBook(RemoveFormView):
    form_class = BookForm
    template_name = "deletebook.html"
    model = Book
    identifier = "isbn"
    successtext = "Book is removed successfully!"
    

class RemoveMember(RemoveFormView):
    form_class = MemberForm
    template_name = "deletemember.html"
    model = Member
    identifier = "member_id"
    successtext = "Member is removed successfully!"


class IssueBook(FormView):
    form_class = TransactionForm
    template_name = "issuebook.html"
    successtext = "Book has been issued successfully!"
    returnURl = 'issueBook'


class ListMember(FormView):
    
    items_per_page = 10

    template_name = "memberslist.html"

    def get(self, request, *args, **kwargs):
        members = Member.objects.all()

        # Create a Paginator object
        paginator = Paginator(members, self.items_per_page)

        # Get the current page number from the request's GET parameters
        current_page = request.GET.get('page')

        # Get the Page object for the current page
        page_obj = paginator.get_page(current_page)        
        
        return render(request, self.template_name, {"page_obj": page_obj})

class ListBook(FormView):
    items_per_page = 10

    template_name = "catalogue.html"

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()

        # Create a Paginator object
        paginator = Paginator(books, self.items_per_page)

        # Get the current page number from the request's GET parameters
        current_page = request.GET.get('page')

        # Get the Page object for the current page
        page_obj = paginator.get_page(current_page)

        return render(request, self.template_name, {'page_obj': page_obj})

class ListTransaction(FormView):

    template_name = "home.html"
    def get(self, request, *args, **kwargs):

        transactions = Transaction.objects.order_by('-transaction_id')[:5]

        return render(request, self.template_name, {"page_obj1": transactions})

