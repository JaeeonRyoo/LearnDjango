from django.db import models

# Create your models here.

class Food(models.Model):
    food_name = models.CharField(max_length=200)
    cooked_date = models.DateTimeField('date cooked')

    def __str__(self):
        return self.food_name

class Tasty(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    tasty_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.tasty_text
