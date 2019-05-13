from django.db import models

# Create your models here.
class join(models.Model):
    email = models.CharField(max_length=100)
    id = models.CharField(max_length=30, primary_key =True)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    reg_date = models.DateField()

    def __str__(self):
        return self.id


class choice(models.Model):
    id = models.CharField(max_length=30 , primary_key =True)
    etc1 = models.CharField(max_length=50)
    etc2 = models.CharField(max_length=50)
    etc3= models.CharField(max_length=50)

    def __str__(self):
        return self.id