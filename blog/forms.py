from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
   class Meta:
        model = Article
        fields = "__all__"


class ContactUsForm(forms.Form):
    nom = forms.CharField(required=False, max_length=200)
    prenom = forms.CharField(max_length=200)
    email = forms.EmailField(required=False)
    message = forms.CharField(max_length=1000)
