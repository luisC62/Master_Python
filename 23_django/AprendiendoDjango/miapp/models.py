from django.db import models

# Create your models here.

# Las migraciones se refieren a los cambios en la estructura de la base de datos
# para poderlas migrar cuando se cree la estructura de producción. 
# Cuando se baje de un repositorio, por ejemplo, se ejecutarán todas las migraciones efectuadas
# de manera que todos tengan la misma base de datos.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Miniatura", upload_to="articles")
    public = models.BooleanField(verbose_name="¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")
    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
    def __str__(self):
        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"
        return f"{self.title}  {public}"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"



    
