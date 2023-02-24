from django.views.generic import DetailView
from django.views.generic import ListView

from author.models import Author


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author
