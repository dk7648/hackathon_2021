
from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render

from reviewapp.models import Review


def review_ownership_required(func):
    def decorated(request, *args, **kwargs):
        review = Review.objects.get(pk=kwargs['pk'])
        if not review.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated


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