import uuid
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Items(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=100, blank=False, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, verbose_name='цена')
    # user = models.ForeignKey(User,blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


