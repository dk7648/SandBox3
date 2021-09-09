from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render

from boardapp.models import Board


def board_ownership_required(func):
    def decorated(request, *args, **kwargs):
        board = Board.objects.get(pk=kwargs['pk'])
        if not board.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated

# 로그인 안하면 로그인페이지로, 학교이메일 아니면 에러 창 표시
# class LoginRequired(AccessMixin):
#     """Verify that the current user is authenticated."""
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()
#         if not 'korea.ac.kr' in request.user.email:
#             return render(request, 'wrong_email.html')
#         return super().dispatch(request, *args, **kwargs)

class LoginRequired(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        try:
            request.user.profile
        except:
            return render(request, 'not_profile.html')
        return super().dispatch(request, *args, **kwargs)