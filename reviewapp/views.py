from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment
from reviewapp.decorators import LoginRequired, review_ownership_required
from reviewapp.form import ReviewCreationForm
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

    def get_context_data(self, **kwargs):
        return super(ReviewCreateView, self).get_context_data(user=self.request.user, **kwargs)
    def get_success_url(self):
        return reverse('reviewapp:detail', kwargs={'pk': self.object.pk})


class ReviewDetailView(LoginRequired, DetailView):
    login_url = '/accounts/login/'
    model = Review
    form_class = CommentCreationForm
    context_object_name = 'target_post'
    template_name = 'reviewapp/detail.html'


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