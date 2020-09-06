from django import forms
from .models import Bookmark, CustomerBookmark
from .models import Customer


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerBookmarkForm(forms.ModelForm):
    class Meta:
        model = CustomerBookmark
        fields = "__all__"
