from django.db import models

class RunningShoe(models.Model):
    brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # e.g., neutral, stability
    cushioning = models.CharField(max_length=50)  # e.g., max, moderate, minimal
    drop_mm = models.FloatField()  # Previously, this was drop_mm, you can rename it if needed
    weight_grams = models.IntegerField()
    surface = models.CharField(max_length=50)  # e.g., road, trail
    foot_strike = models.CharField(max_length=50)  # e.g., forefoot, midfoot, heel
    pronation_support = models.BooleanField()
    image_url = models.URLField(blank=True)
    stack_height = models.IntegerField()  # Added field
    heel_to_toe_drop = models.IntegerField()  # Added field
    best_for = models.CharField(max_length=100)  # Added field

    def __str__(self):
        return f"{self.brand} {self.model_name}"
