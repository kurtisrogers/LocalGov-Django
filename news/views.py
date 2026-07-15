"""News views."""

from django.views.generic import DetailView, ListView

from core.views import get_published_or_404
from news.models import NewsArticle, Newsroom


class NewsroomListView(ListView):
    model = Newsroom
    template_name = "news/newsroom_list.html"
    context_object_name = "newsrooms"

    def get_queryset(self):
        return Newsroom.objects.filter(published=True)


class NewsroomDetailView(DetailView):
    model = Newsroom
    template_name = "news/newsroom_detail.html"
    context_object_name = "newsroom"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(Newsroom, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = self.object.articles.filter(published=True)
        context["featured_articles"] = articles.filter(featured=True)[:3]
        context["articles"] = articles
        category = self.request.GET.get("category", "")
        year = self.request.GET.get("year", "")
        if category:
            context["articles"] = context["articles"].filter(categories__slug=category)
        if year:
            context["articles"] = context["articles"].filter(published_date__year=year)
        context["selected_category"] = category
        context["selected_year"] = year
        return context


class NewsArticleDetailView(DetailView):
    model = NewsArticle
    template_name = "news/article_detail.html"
    context_object_name = "article"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(
            NewsArticle,
            slug=self.kwargs["slug"],
            newsroom__slug=self.kwargs["newsroom_slug"],
            published_date__year=self.kwargs["year"],
            newsroom__published=True,
        )
