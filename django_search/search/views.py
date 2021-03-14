from django.shortcuts import render
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .models import Article
from .forms import SearchForm


def article_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = Article.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by('-rank')

    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})
