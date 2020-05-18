from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article
import datetime

# Create your views here.
def index(request):
    articles = Article.objects.all()
    movies = Article.objects.filter(category="movie")
    dramas = Article.objects.filter(category="drama")
    entertains = Article.objects.filter(category="entertain")
    movie_num = len(movies)
    drama_num = len(dramas)
    entertain_num = len(entertains)
    return render(request, 'index.html', {
        'articles' : articles,
        'movie_num' : movie_num,
        'drama_num' : drama_num,
        'entertain_num' : entertain_num})

def detail(request, post_pk):
    article = Article.objects.get(pk=post_pk)
    return render(request, 'detail.html', {
        'article' : article
        })

def new(request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            time = datetime.datetime.now()
        )
        return redirect('detail_name', new_article.pk)
    else:
        return render(request, 'new.html')

def movie(request):
    movies = Article.objects.filter(category="movie")
    return render(request, 'movie.html', {'movies' : movies})

def drama(request):
    dramas = Article.objects.filter(category="drama")
    return render(request, 'drama.html', {'dramas' : dramas})

def entertain(request):
    entertains = Article.objects.filter(category="entertain")
    return render(request, 'entertain.html', {'entertains' : entertains})