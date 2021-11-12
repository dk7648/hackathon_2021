from django.urls import path

from roomapp.views import RoomCreateView, RoomUpdateView

app_name = "roomapp"

urlpatterns = [
    path('create/', RoomCreateView.as_view(), name='create'),
    path('update/<int:pk>', RoomUpdateView.as_view(), name='update'),
]