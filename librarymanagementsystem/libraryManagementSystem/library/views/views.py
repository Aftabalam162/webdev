from ..forms import LibrarianForm, BookForm, MemberForm, BookIssueForm, TransactionForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required


class FormView(View):
    form_class = None
    template_name = None
    success_url = "success_url"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        return self.success_url


class Book(FormView):
    form_class = BookForm
    template_name = 'addbook.html'


class BookIssue(FormView):
    form_class = BookIssueForm
    template_name = 'addreturnentry.html'


class Transaction(FormView):
    form_class = TransactionForm
    template_name = 'addtransaction.html'


class Member(FormView):
    form_class = MemberForm
    template_name = 'addmember.html'
