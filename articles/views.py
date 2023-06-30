from .models import Article
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/home.html'
    ordering = ['-date_posted']
    paginate_by = 8


class ArticleView(DetailView):
    model = Article


class ArticleCreate(CreateView, LoginRequiredMixin):
    model = Article
    fields = ['title', 'headline', 'image', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleEdit(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Article
    fields = ['title', 'headline', 'image', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ArticleDelete(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Article
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



