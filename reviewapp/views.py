from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment
from reviewapp.decorators import review_ownership_required, LoginRequired
from reviewapp.forms import ReviewCreationForm
from reviewapp.models import Review


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewCreationForm
    template_name = 'reviewapp/create.html'

    def form_valid(self, form):
        temp_review = form.save(commit=False)
        temp_review.writer = self.request.user
        temp_review.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reviewapp:detail', kwargs={'pk': self.object.pk})



class ReviewDetailView(LoginRequired, DetailView, FormMixin):
    login_url = '/accounts/login/'
    model = Review
    form_class = CommentCreationForm
    context_object_name = 'target_post'
    template_name = 'reviewapp/detail.html'

    def get_context_data(self, **kwargs):
        comment_list = Comment.objects.filter(review=self.object.pk).order_by('-created_at')
        # if user.is_authenticated: #로그인 했는가?
        # join = Join.objects.filter(user=user, project=project)
        # object_list = Post.object(project=self.get_object())
        return super(ReviewDetailView, self).get_context_data(comment_list=comment_list, **kwargs)


@method_decorator(review_ownership_required, 'get')
@method_decorator(review_ownership_required, 'post')
class ReviewUpdateView(UpdateView):
    model = Review
    context_object_name = 'target_post'
    form_class = ReviewCreationForm
    template_name = 'reviewapp/update.html'

    def get_success_url(self):
        return reverse('reviewapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(review_ownership_required, 'get')
@method_decorator(review_ownership_required, 'post')
class ReviewDeleteView(DeleteView):
    model = Review
    context_object_name = 'target_post'
    success_url = reverse_lazy('reviewapp:list')
    template_name = 'reviewapp/delete.html'


class ReviewListView(LoginRequired, ListView):
    login_url = '/accounts/login/'
    model = Review
    context_object_name = 'post_list'
    # ordering = ['-id']
    template_name = 'reviewapp/list.html'

    def get_queryset(self):
        all_list = Review.objects.filter().order_by('-id')

        page = int(self.request.GET.get('page', 1))
        paginator = Paginator(all_list, 4)
        queryset = paginator.get_page(page)

        return queryset

