from django.contrib import admin
from catalogo_app.models import Catalogo, Categoria, Tipo_Archivo, Tipo_Imagen, Orientacion, Permisos, Perspectiva, Tag


class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('id','catalogo')


class Tipo_ArchivoAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_archivo')


class Tipo_ImagenAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_imagen')


class OrientacionAdmin(admin.ModelAdmin):
    list_display = ('id','orientacion')


class PermisosAdmin(admin.ModelAdmin):
    list_display = ('id','permisos')


class PerspectivaAdmin(admin.ModelAdmin):
    list_display = ('id','perspectiva')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id','tag')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','categoria')

admin.site.register(Tipo_Archivo)
admin.site.register(Tipo_Imagen)
admin.site.register(Orientacion)
admin.site.register(Permisos)
admin.site.register(Perspectiva)
admin.site.register(Tag)
admin.site.register(Catalogo)
admin.site.register(Categoria, CategoriaAdmin)

