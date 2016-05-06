from django.views.generic import ListView
from django.views.generic import DetailView
from pure_pagination.mixins import PaginationMixin

from catalogo_app.models import Catalogo


class CatalogoListView(PaginationMixin, ListView):
    model = Catalogo
    template_name = 'catalogo_app/list.html'
    paginate_by = 30

    def get_context_data(self, **kwargs):

        context = super(CatalogoListView, self).get_context_data(**kwargs)

        context['backlist'] = 'large'

        return context


class CatalogoView(DetailView):
    model = Catalogo
    template_name = 'catalogo_app/view.html'
