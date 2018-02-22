from django.shortcuts import render,get_object_or_404
from models import *
from comment.forms import CommentForm

def index(request):
    article_list = Article.objects.all().order_by('create_time')
    context = {'article_list':article_list,}
    return render(request,'blog/index.html',context)

def detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    form = CommentForm()
    comment_list = article.mycomment_set.all()
    context = {'article':article,'form':form,'comment_list':comment_list}
    return render(request,'blog/detail.html',context)

def guidang(request,year,month):
    article_list = Article.objects.filter(create_time__year=year,create_time__month=month).order_by("-create_time")
    context = {'article_list':article_list}
    return render(request,'blog/index.html',context)

def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    article_list = Article.objects.filter(category=cate).order_by('-create_time')
    context = {'article_list':article_list}
    return render(request,'blog/index.html',context)
