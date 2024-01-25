from django.db import models

# Create your models here.
class Banner(models.Model):
    img = models.ImageField(upload_to='img')
    titulo = models.CharField(max_length=50, null=True)
    texto = models.TextField()
    def __str__(self) -> str:
        return self.titulo
