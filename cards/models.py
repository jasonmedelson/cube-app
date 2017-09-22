from django.db import models

# Create your models here.
class Cubelist(models.Model):
    card_id = models.BigAutoField(primary_key=True)
    card_name = models.CharField(max_length=150)
    card_cost = models.SmallIntegerField(blank=True, null=True)
    card_image = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'cubeList'
    def __str__(self):
        return self.card_name