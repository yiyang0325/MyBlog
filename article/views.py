from django.shortcuts import render

from .models import Article
# Create your views here.

def allArticles(request):
	articles = Article.objects.all()

	context = {
		'articles': articles,
	}
	return render(request, "home.html", context)