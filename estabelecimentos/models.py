from django.db import models
from django.urls import reverse

# Create your models here.
class Imagem(models.Model):
    img = models.ImageField(upload_to='img')
    def __str__(self) -> str:
        return self.img.url
    
class Cidade(models.Model):
    nome = models.CharField(max_length=30)
    img = models.ImageField(upload_to='img')
    def __str__(self) -> str:
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    img = models.ImageField(upload_to='img')
    def __str__(self) -> str:
        return self.nome
    
class subCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.nome
    
class Estabelecimento(models.Model):    
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    tiktok = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    subCategoria = models.ForeignKey(subCategoria, on_delete=models.DO_NOTHING)
    rua = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    mapa = models.TextField()
    descricao = models.TextField()
    imagens = models.ManyToManyField(Imagem)
    video = models.TextField()
    slug = models.SlugField(null=False, unique=True)  # new
    destaque = models.BooleanField(default=False)
        
    def __str__(self) -> str:
        return self.rua
    
    def get_absolute_url(self):
        return reverse("estabelecimento", kwargs={"slug": self.slug})