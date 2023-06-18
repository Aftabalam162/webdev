from ..forms import BookForm, MemberForm, BookIssueForm, TransactionForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect


class FormView(View):
    form_class = None
    template_name = None
    successtext = None
    returnURl = None

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            try: 
                form.save()
            except ValueError as e:
                messages.error(request, str(e), extra_tags='danger')
                return render(request, self.template_name, {'form': form})
            
            messages.success(request, self.successtext, extra_tags='success')  
            return HttpResponseRedirect(reverse(self.returnURl))
        return render(request, self.template_name, {'form': form})



class Book(FormView):
    form_class = BookForm
    template_name = 'addbook.html'
    successtext = "Book is added successfully!"
    returnURl = 'addBook'


class BookIssue(FormView):
    form_class = BookIssueForm
    template_name = 'addreturnentry.html'
    successtext = "Return entry is added successfully!"
    returnURl = 'addReturnEntry'


class Transaction(FormView):
    form_class = TransactionForm
    template_name = 'addtransaction.html'
    successtext = "Issue entry is added successfully!"
    returnURL = 'addTransaction'


class Member(FormView):
    form_class = MemberForm
    template_name = 'addmember.html'
    successtext = "Member is added successfully!"
    returnURl = 'addMember'



