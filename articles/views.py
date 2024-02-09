from django.shortcuts import render
from .forms import ArticleCommentForm
from .models import Article, ArticleComment



def articles_view(request):
    articles = Article.objects.order_by("created")
    articles_short = [article.text_part[:100] for article in articles]
    return render(request, 'articles/all_articles.html', {'articles': articles, 'article_short': articles_short})


def article_view(request, id):
    article = Article.objects.get(id=id)
    form = ArticleCommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()
        form = ArticleCommentForm()
    
    comments = ArticleComment.objects.filter(article=article).order_by("created")
    return render(request, 'articles/article.html', {'article': article,
                                                     'comments': comments,
                                                     'form': form})
