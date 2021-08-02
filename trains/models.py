from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='train name')
    travel_time = models.PositiveSmallIntegerField(verbose_name='time on a road')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set', verbose_name='from which city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city_set', verbose_name='to which city')


    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('change city incoming')
        qs = Train.objects.filter(from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('change time on road')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)



    def __str__(self):
        return f'Train #{self.name} from city {self.from_city}'

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        ordering = ['travel_time']
