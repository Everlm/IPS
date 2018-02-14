import django_filters
from AreaOftalmologia.models import Ciudad

class CiudadFilter(django_filters.FilterSet):

    departamento=django_filters.CharFilter(name='departamento.codigo')

    class Meta:
        model = Ciudad
        fields =('departamento', 'codigo', 'nombre')
