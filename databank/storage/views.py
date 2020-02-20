# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from storage.forms import ItemForm
from storage.models import Source, Item


class SourceCreateView(generic.CreateView):
    model = Source
    template_name = 'storage/source_create.html'
    fields = ['name', 'url', 'description']
    success_url = reverse_lazy('storage:source-create')


class SourceListView(generic.ListView):
    model = Source
    context_object_name = 'sources'


class ItemCreateView(LoginRequiredMixin,
                     generic.FormView):
    form_class = ItemForm
    template_name = 'storage/item_create.html'
    success_url = reverse_lazy('storage:item-create')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super(ItemCreateView, self).form_valid(form)


class ItemListView(generic.ListView):
    model = Item
    context_object_name = 'items'


class ItemDetailView(generic.DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sample'] = "Use the power of generic views"
        return context


class ItemUpdateView(generic.UpdateView):
    model = Item
    fields = ['name', 'description']
    template_name = 'storage/item_update.html'


class ItemDelete(generic.DeleteView):
    model = Item
    success_url = reverse_lazy('storage:item-list')
    template_name = 'storage/item_delete.html'

