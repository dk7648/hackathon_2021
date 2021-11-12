from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView

from reviewapp.decorators import LoginRequired
from roomapp.decorators import room_ownership_required
from roomapp.forms import RoomCreationForm
from roomapp.models import Room


class RoomIndexView(ListView):
    model = Room
    context_object_name = 'room_list'
    template_name = 'roomapp/list.html'


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomCreationForm
    template_name = 'roomapp/create.html'

    def form_valid(self, form):
        temp_room = form.save(commit=False)
        temp_room.user = self.request.user
        temp_room.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})


@method_decorator(room_ownership_required, 'get')
@method_decorator(room_ownership_required, 'post')
class RoomUpdateView(UpdateView):
    model = Room
    context_object_name = 'target_room'
    form_class = RoomCreationForm
    template_name = 'roomapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})