from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode(self.id)


class Tipo_Archivo(models.Model):
    tipo_archivo = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode(self.id)


class Tipo_Imagen(models.Model):
    tipo_imagen = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode(self.id)


class Orientacion(models.Model):
    orientacion = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode(self.id)


class Permisos(models.Model):
    permisos = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode(self.id)


class Perspectiva(models.Model):
    perspectiva = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode(self.id)


class Tag(models.Model):
    tag = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode(self.id)


class Catalogo(models.Model):
    image = models.FileField(upload_to="Archivos/", default='None')
    descripcion = models.TextField()
    claves = models.TextField()
    tipo_archivo = models.ForeignKey(Tipo_Archivo, default=1)
    categoria = models.ForeignKey(Categoria)
    tipo_imagen = models.ForeignKey(Tipo_Imagen, default=1)
    orientacion = models.ForeignKey(Orientacion, default=1)
    autor = models.CharField(max_length=256)
    fuente = models.CharField(max_length=256)
    permisos = models.ForeignKey(Permisos, default=1)
    personas = models.BooleanField(default=False)
    color = models.BooleanField(default=False)
    fecha = models.DateField()
    lugar = models.CharField(max_length=256)
    ancho = models.CharField(max_length=256)
    largo = models.CharField(max_length=256)
    perspectiva = models.ForeignKey(Perspectiva, default=1)
    tag = models.ManyToManyField(Tag, default=1)

    def __unicode__(self):
        return unicode(self.id)
