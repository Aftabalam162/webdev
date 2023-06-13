from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import Librarian, Book, Member, BookIssue, Transaction

class LibrarianForm(View):
    form_class = Librarian
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'addLibrarian.html', {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            # Process form cleaned data
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, 'addLibrarian.html', {'form': form})
    
class BookForm(View):
    form_class = Book
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'addBook.html', {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            # Process form cleaned data
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, 'addBook.html', {'form': form})
    
class BookIssueForm(View):
    form_class = BookIssue
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'addReturnEntry.html', {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            # Process form cleaned data
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, 'addReturnEntry.html', {'form': form})
    

class TransactionForm(View):
    form_class = Transaction
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'addTransaction.html', {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            # Process form cleaned data
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, 'addTransaction.html', {'form': form})
    

class MemberForm(View):
    form_class = Member
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'addMember.html', {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            # Process form cleaned data
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, 'addMember.html', {'form': form})