from django.contrib import admin
from .models import Librarian, Book, Member, BookIssue, Transaction

# Register your models here.

admin.site.register(Librarian)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(BookIssue)
admin.site.register(Transaction)
