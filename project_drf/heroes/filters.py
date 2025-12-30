import django_filters
from .models import Hero


class HeroFilter(django_filters.FilterSet):
    power = django_filters.CharFilter(field_name='power',lookup_expr='iexact')
    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    id=django_filters.RangeFilter(field_name='id')
    
    class Meta:
        model = Hero
        fields = ['power' ,'name']
        