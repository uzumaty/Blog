from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name="Imagen")
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-fecha_creacion"]
        
        
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        