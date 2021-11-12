
from django.urls import path

from reviewapp.views import ReviewCreateView, ReviewUpdateView, ReviewDetailView, ReviewDeleteView, ReviewListView

app_name = "reviewapp"

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='create'),
    path('update/<int:pk>', ReviewUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', ReviewDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', ReviewDeleteView.as_view(), name='delete'),

    path('list/', ReviewListView.as_view(), name='list'),
]