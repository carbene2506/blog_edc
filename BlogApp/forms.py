from django import forms

from .models import Blog

class BlogForm(forms.ModelForm):  #form.modleform is a module from which our class extracts
    class Meta:                     #predefined class
        model = Blog
        fields = ['username', 'text']  #yaha par forms mein input lene ke liye diye hai