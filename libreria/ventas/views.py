from django.views.generic import ListView, DetailView
from catalogo.models import Libro

class StoreView(ListView):
    model = Libro
    template_name = 'ventas/store.html'
    context_object_name = 'libros'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        autor = self.request.GET.get('autor', '')
        libros = Libro.objects.filter(stock__gt=0)
        if query:
            libros = libros.filter(titulo__icontains=query)
        if autor:
            libros = libros.filter(autor__nombre__icontains=autor)
        return libros

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['autor'] = self.request.GET.get('autor', '')
        return context

class BookDetailView(DetailView):
    model = Libro
    template_name = 'ventas/book_detail.html'
    context_object_name = 'libro'
