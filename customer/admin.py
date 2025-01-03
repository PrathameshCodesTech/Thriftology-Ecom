from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'locality', 'city', 'zipcode', 'state')
    search_fields = ('name', 'city', 'state')
    list_filter = ('state',)

