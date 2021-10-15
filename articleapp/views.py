# Create your views here.
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from projectapp.models import Project


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})
    #자신이 만든 프로젝트에만 article을 작성하게 해주는 method
    def get_form(self, form_class=None):
        form = super(ArticleCreateView, self).get_form()
        form.fields['project'].queryset = Project.objects.filter(writer_id=self.request.user.id)
        return form


class ArticleDetailView(DetailView,FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'targetArticle'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'targetArticle'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(article_ownership_required,'post')
@method_decorator(article_ownership_required,'get')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'targetArticle'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 5
