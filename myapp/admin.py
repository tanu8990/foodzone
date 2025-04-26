from django.contrib import admin
from myapp.models import Contact
from myapp.models import Table
from .models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Table)
admin.site.register(CategoryA)
admin.site.register(ProductA)
admin.site.register(Team)
