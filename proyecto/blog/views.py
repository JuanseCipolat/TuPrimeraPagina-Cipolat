from . import forms
from . import models
from django.shortcuts import render, redirect



def index(request):
    return render(request, "blog/index.html")

def post_list(request):
    posts = models.Post.objects.all()
    contexto = {'posts': posts}
    return render(request, 'blog/post_list.html', contexto)


def post_create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = forms.PostForm()
    return render(request, "blog/post_create.html" , {'form': form})
    