
from django.http import HttpResponseForbidden

from articleapp.models import Article

#고유한 pk값에 해당하는 Article의 객체를 얻어 article 변수에 저장한다.


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)

    return decorated