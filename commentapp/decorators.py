
from django.http import HttpResponseForbidden

from articleapp.models import Article

#고유한 pk값에 해당하는 Article의 객체를 얻어 article 변수에 저장한다.
from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)

    return decorated