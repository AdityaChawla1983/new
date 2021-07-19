from django.contrib.auth.mixins import (
LoginRequiredMixin,
UserPassesTestMixin # new
)
from django.http import response
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def user_logout(request):
    logout(request)
    return response.HttpResponseRedirect('home')




def redirect_view(request):
        response = redirect('/redirect-success/')
        return response
class ArticleListView(LoginRequiredMixin, ListView): # new
    model = Article
    template_name = 'article_list.html'
    login_url = 'login' # new
class ArticleDetailView(LoginRequiredMixin, DetailView): # new
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login' # new
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #new
    model = Article
    fields = ('title', 'body',  'mainphoto',)
    template_name = 'article_edit.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'mainphoto',)
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self):
            obj = self.get_object()
            return obj.author == self.request.user  
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)