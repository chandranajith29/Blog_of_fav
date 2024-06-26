from django.shortcuts import render,get_object_or_404
from .models import post,Comment

# Create your views here.
def home(request):
    all_posts=post.objects.all()
    # all_category=categories.objects.all()
    return render(request,"home.html",{"posts":all_posts})
def details(request,pk):
    posts=post.objects.get(id=pk)
    if request.method=="POST":
        auth_name=request.POST.get("auth_name")
        post_com=request.POST.get("post_Comment")
        Comment.objects.create(author=auth_name,body=post_com,post_id=pk)

    Comments=Comment.objects.filter(post_id=pk)
    context={
        "i":posts,
        "comments":Comments
    }
    return render(request,"details1.html",context)
