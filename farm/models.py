from django.db import models

class products(models.Model):
    name=models.CharField(max_length=1000)
    image=models.CharField(max_length=1000)
    quantity=models.CharField(max_length=1000)
    cost=models.CharField(max_length=1000)

    def __str__(self):
        return  self.name+"  "+self.cost
