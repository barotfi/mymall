from django import forms

from .models import Stores

class Newstoreform(forms.ModelForm):

    class Meta:
        model = Stores
        fields = ('category', 'storename', 'store_link', 'store_username', 'store_pw')
