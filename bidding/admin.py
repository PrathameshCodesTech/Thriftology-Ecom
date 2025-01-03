from django import forms
from django.contrib import admin
from .models import Bid, NewArrival
from django.contrib.auth.models import User

class BidAdminForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the user field to only include admin users
        self.fields['user'].queryset = User.objects.filter(is_staff=True)

class BidAdmin(admin.ModelAdmin):
    form = BidAdminForm
    list_display = ('user', 'new_arrival', 'amount', 'timestamp')
    search_fields = ('user__username', 'new_arrival__product__name')

class NewArrivalAdmin(admin.ModelAdmin):
    list_display = ('product', 'start_date', 'end_date')
    search_fields = ('product__name',)

admin.site.register(NewArrival, NewArrivalAdmin)
admin.site.register(Bid, BidAdmin)