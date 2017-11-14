# Form for menus.


from django import forms
from .models import Item
from restaurants.models import RestaurantLocation


class ItemForm(forms.ModelForm):
    """Item Entry Form"""

    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        print(kwargs)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner=user)
