from django import forms
from news.models.user_model import Users
from news.models.category_model import Categories


class CreateCategoriesForm(forms.Form):
    name = forms.CharField(max_length=200)


class CreateNewsForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(
        queryset=Users.objects.all()
    )
    created_at = forms.DateField()
    image = forms.ImageField()
    categories = forms.ModelMultipleChoiceField(
        queryset=Categories.objects.all()
    )
