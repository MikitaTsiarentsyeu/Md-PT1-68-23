from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Post
from .forms import AddPostFreeForm, AddPostModelForm
from django.contrib.auth.decorators import permission_required


# Create your views here.
def test(request):
    now = datetime.now()
    print(now)
    return render(request, 'test.html', {'time':now})

def posts(request):
    posts = Post.objects.all()
    viewed_posts = request.session.get("viewed_posts", [])
    return render(request, 'posts.html', {'posts':posts, 'viewed_posts':viewed_posts})


def post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)

        viewed_posts = request.session.get("viewed_posts", [])
        if p.id not in viewed_posts:
            viewed_posts.append(p.id)

        request.session["viewed_posts"] = viewed_posts

        return render(request, 'post.html', {'p': p})
    except:
        # return HttpResponse(f"<h3>Cannot find the post</h3>")
        return HttpResponseNotFound()
    
def add_free(request):

    if request.method == 'POST':
        form = AddPostFreeForm(request.POST, request.FILES)
        
        if form.is_valid():
            post_entry = Post()
            post_entry.title = form.cleaned_data['title']
            post_entry.content = form.cleaned_data['content']
            post_entry.post_type = form.cleaned_data['post_type']
            post_entry.image = form.cleaned_data['image']
            post_entry.author = Author.objects.all()[0]
            post_entry.save()

            return redirect('post', post_entry.id)
        else:
            pass

    else:
        form = AddPostFreeForm()

    return render(request, 'add_free_form.html', {'form':form})

@permission_required('main.add_post')
def add_model(request):

    if request.method == 'POST':
        form = AddPostModelForm(request.POST, request.FILES)
        
        if form.is_valid():
            post_entry = form.save(commit=False)
            try:
                post_entry.author = Author.objects.get(email=request.user.email)
            except:
                post_entry.author = Author.objects.all()[0]
            post_entry.save()

            return redirect('post', post_entry.id)
        else:
            pass

    else:
        form = AddPostModelForm()

    return render(request, 'add_free_form.html', {'form':form})