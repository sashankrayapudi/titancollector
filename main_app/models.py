from django.db import models
from django.urls import reverse

from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)



class Eldian(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('eldians_detail', kwargs={'pk': self.id})

class Titan(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    eldians = models.ManyToManyField(Eldian)

    def __str__(self):
      return self.name


    def get_absolute_url(self):
      return reverse('detail', kwargs={'titan_id': self.id})

    def meals_left(self):
      return 5 - self.feeding_set.filter(date=date.today()).count()


class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )

  # create titan_id FK since Feeding must hold ID of the titan object it belongs to
  titan = models.ForeignKey(Titan, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_meal_display()} on {self.date}'

  class Meta:
    ordering = ['-date']

