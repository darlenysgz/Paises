from django.shortcuts import get_object_or_404, render
from .models import pais, ciudad
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    model = pais
    template_name = 'Paises/index.html'
    context_object_name = 'Agregado_Reciente'

    def get_queryset(self):
        return pais.objects.all()

class DetailView(generic.DetailView):
    model = pais
    template_name = 'Paises/detail.html'


class Resultados(generic.DetailView):
    model = pais
    template_name = 'Paises/resultados.html'

def ciudades(request, id_pais):
    p = get_object_or_404(pais, pk = id_pais)
    try:
        ciudad_seleccionada = p.ciudad_set.get(pk = request.POST['ciudad'])
    except (KeyError, ciudad.DoesNotExist):
        return render(request, 'Paises/detail.html', {
            'pais': p,
            'error_message': "No has seleccionada nada.",
        })
    else:
        ciudad_seleccionada.save()
        return render(request,'Paises/resultados.html', {'pais':p})
