from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='route name')
    travel_times = models.PositiveSmallIntegerField(verbose_name='time on a road')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set', verbose_name='from which city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_to_city_set', verbose_name='to which city')
    trains = models.ManyToManyField(Train, verbose_name='List of trains')


    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('change city incoming')
        qs = Train.objects.filter(from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_times).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('change time on road')




    def __str__(self):
        return f'Route {self.name} from city {self.from_city}'

    class Meta:
        verbose_name = 'Rout'
        verbose_name_plural = 'Routes'
        ordering = ['travel_times']
