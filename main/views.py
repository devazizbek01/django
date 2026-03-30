from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import NewPost



def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts

    }
    return render(request, 'index.html', context)




def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "detail.html", {'post':post})



def create_post(request):
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = NewPost()
        return render(request, 'create.html', {'form': form})
    







def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = NewPost(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', post_id=post.id)
    else:
        form = NewPost(instance=post)
        return render(request, 'edit.html', {'form': form, 'post':post})
