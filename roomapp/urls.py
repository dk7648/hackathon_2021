from django.urls import path

from roomapp.views import RoomCreateView, RoomUpdateView, RoomIndexView

app_name = "roomapp"

urlpatterns = [
    path('create/', RoomCreateView.as_view(), name='create'),
    path('update/<int:pk>', RoomUpdateView.as_view(), name='update'),
    path('list/', RoomIndexView.as_view(), name='list'),
]