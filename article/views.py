from typing import Mapping
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.urls import reverse
from .forms import articleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.


def articles(request):
    articles = Article.objects.all()
    return render(request,"articles.html",{"articles":articles})





def index(request):
    context={
        "no1":1,
        "no2":2,
        "no3":3,
        "no4":4,
        "no5":5
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context={
        "articles":articles
        }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addArticle(request):
    form = articleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Article has been successfuly created.")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})
def detail(request,id):
    context=get_object_or_404(Article,id=id)
    comments = context.comments.all()
    return render(request,"detail.html",{"article":context,"comments":comments})
@login_required(login_url="user:login")
def update(request,id):
    article=get_object_or_404(Article,id=id)
    form = articleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
         article=form.save(commit=False)
         article.author = request.user
         article.save()
         return redirect("index")

    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")
def delete(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Article has been deleted.")
    return redirect("article:dashboard")
def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    
    if request.method == "POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")

        newComment=Comment(comment_author = comment_author,comment_content=comment_content,)
        newComment.article=article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))