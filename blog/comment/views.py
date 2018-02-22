from django.shortcuts import render,redirect,get_object_or_404
from myblog.models import Article
from .models import Mycomment
from .forms import CommentForm


def article_comment(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.Form)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(article)
        else:

            comment_list = post.comment_set.all()
            context = {'article': article,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
        return redirect(article)
