from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Tag)