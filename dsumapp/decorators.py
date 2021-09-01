from django.http import HttpResponseForbidden

from dsumapp.models import Dsum
from postapp.models import Post


def dsum_ownership_required(func):
    def decorated(request, *args, **kwargs):
        dsum = Dsum.objects.get(pk=kwargs['pk'])
        if not dsum.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated