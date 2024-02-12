from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):    
    titulo = models.CharField(max_length=50)    
    descricao = RichTextField()
    img = models.ImageField(upload_to='img_about')
    img_video = models.ImageField(upload_to='img_about_video', null=True)
    lnk_video = models.CharField(max_length=50, null = True)    

        
    def __str__(self) -> str:
        return self.titulo
    
    
