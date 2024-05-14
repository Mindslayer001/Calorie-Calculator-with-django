from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    serving_size_g = models.FloatField()
    calories = models.FloatField()
    carbohydrates_total_g = models.FloatField()
    protein_g = models.FloatField()
    fat_total_g = models.FloatField()
    sugar_g = models.FloatField()
    fiber_g = models.FloatField()
    sodium_mg = models.FloatField()
    potassium_mg = models.FloatField()
    fat_saturated_g = models.FloatField()
    cholesterol_mg = models.FloatField()

    def __str__(self):
        return self.name
