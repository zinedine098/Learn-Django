from django.shortcuts import get_object_or_404, redirect, render
from django.template.context_processors import request
from . import models
from . import forms

# Create your views here.
def home(request):
    post = models.Post.objects.all()
    return render(request, "Blog/Home/index.html", {
        'post': post
    })
    
def postDetail(request, id):
    post = get_object_or_404(models.Post, id=id)
    return render(request, "Blog/Home/detail.html", {
        'post': post
    })
    
def createPost(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post-detail', id=post.id)
    else:
        form = forms.PostForm()
    return render(request, 'Blog/Home/create_post.html', {'form': form})