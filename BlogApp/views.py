from django.shortcuts import redirect, render

from .models import Blog
from .forms import BlogForm

# Create your views here.
def create_blog(request):
    if request.method == 'POST':   # A type of form submission of data by the user
        form = BlogForm(request.POST)  #request.post is the data

        if form.is_valid():
            form.save()  #object id and date are created while saving
            #blog.save()

            return redirect('/blog/display')
    else :
        form = BlogForm() #just an empty form for safety measures

    return render(request, 'createBlog.html', {'form' : form})  #form without quotes is the data

def display_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'displayBlogs.html', {'blogs': blogs})