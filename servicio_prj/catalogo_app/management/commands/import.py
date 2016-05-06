# coding=utf-8
from django.core.management.base import BaseCommand
from catalogo_app.models import Tipo_Archivo, Categoria, Tipo_Imagen, Orientacion, Permisos, Perspectiva, Catalogo


class Command(BaseCommand):

    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument('--importar_catalogo',
                            action='store_true',
                            dest='importar_catalogo',
                            default=False,
                            help='Importa archivos del catalogo')

        parser.add_argument('--importar_tipo_archivo',
                            action='store_true',
                            dest='importar_tipo_archivo',
                            default=False,
                            help='Importa registros de tipo de archivo')

        parser.add_argument('--importar_categoria',
                            action='store_true',
                            dest='importar_categoria',
                            default=False,
                            help='Importa clasificacion de la categoria del archivo: divulgacion, cientifico...')

        parser.add_argument('--importar_tipo_imagen',
                            action='store_true',
                            dest='importar_tipo_imagen',
                            default=False,
                            help='Importa registros de la naturaleza de la imagen foto, ilustracion, logo...')

        parser.add_argument('--importar_orientacion',
                            action='store_true',
                            dest='importar_orientacion',
                            default=False,
                            help='Importa orientacion del archivo: vertical, horizontal, cuadrado')

        parser.add_argument('--importar_permisos',
                            action='store_true',
                            dest='importar_permisos',
                            default=False,
                            help='Importa tipo de permiso de reproduccion del archivo')

        parser.add_argument('--importar_perspectiva',
                            action='store_true',
                            dest='importar_perspectiva',
                            default=False,
                            help='Importa perspectiva de la imagen del archivo')

        parser.add_argument('--enviar_correo',
                            action='store_true',
                            dest='enviar_correo',
                            default=False,
                            help='Prueba para enviar correo')

        parser.add_argument('archivo')

    def handle(self, *args, **options):
        # ...
        if options['importar_catalogo']:
            """
            Comando para importar el catalogo
            """

            archivo = options['archivo']
            fileHandle = open(archivo)
            fileList = fileHandle.readlines()

            for fileLine in fileList:
                [catalogo, catalogo] = fileLine.split("|")
                A = catalogo.strip(' \t\n\r')
                B = catalogo.strip(' \t\n\r')
                C = catalogo.strip(' \t\n\r')
                D = catalogo.strip(' \t\n\r')
                E = catalogo.strip(' \t\n\r')
                F = catalogo.strip(' \t\n\r')
                print catalogo

                try:
                    # ojo para la imagen grabar de la siguinete manera image = 'image/'+image
                    catalogo = Catalogo(id=A, tipo_archivo=tipo_archivo)
                    catalogo = Catalogo(id=B, categoria=categoria)
                    catalogo = Catalogo(id=C, tipo_imagen=tipo_imagen)
                    catalogo = Catalogo(id=D, orientacion=orientacion)
                    catalogo = Catalogo(id=E, permisos=permisos)
                    catalogo = Catalogo(id=F, perspectiva=perspectiva)
                    catalogo = Catalogo(id=catalogo_id, catalogo=catalogo)
                    catalogo.save()

                except:
                    print "Ocurrio un error al intentar grabar"
                    break

        if options['importar_tipo_archivo']:
            """
            Comando para importar tipo archivo
            """

            archivo = options['archivo']
            fileHandle = open(archivo)
            fileList = fileHandle.readlines()

            for fileLine in fileList:
                [tipo_archivo_id, tipo_archivo] = fileLine.split("|")
                tipo_archivo = tipo_archivo.strip(' \t\n\r')
                print tipo_archivo_id, tipo_archivo

                try:
                    # ojo para la imagen grabar de la siguinete manera image = 'image/'+image
                    tipo_archivo = Tipo_Archivo(id=tipo_archivo_id, tipo_archivo=tipo_archivo)
                    tipo_archivo.save()

                except:
                    print "Ocurrio un error al intentar grabar"
                    break

        if options['importar_categoria']:
            """
            Comando para importar categoria del archivo
            """

            archivo = options['archivo']
            fileHandle = open(archivo)
            fileList = fileHandle.readlines()

            for fileLine in fileList:
                [categoria_id, categoria] = fileLine.split("|")
                categoria = categoria.strip(' \t\n\r')
                print categoria_id, categoria

                try:
                    # ojo para la imagen grabar de la siguinete manera image = 'image/'+image
                    categoria = Categoria(id=categoria_id, categoria=categoria)
                    categoria.save()

                except:
                    print "Ocurrio un error al intentar grabar"
                    break

        if options['importar_tipo_imagen']:
            """
            Comando para importar tipo archivo
            """

            archivo = options['archivo']
            fileHandle = open(archivo)
            fileList = fileHandle.readlines()

            for fileLine in fileList:
                [tipo_imagen_id, tipo_imagen] = fileLine.split("|")
                tipo_imagen = tipo_imagen.strip(' \t\n\r')
                print tipo_imagen_id, tipo_imagen

                try:
                    # ojo para la imagen grabar de la siguinete manera image = 'image/'+image
                    tipo_imagen = Tipo_Imagen(id=tipo_imagen_id, tipo_imagen=tipo_imagen)
                    tipo_imagen.save()

                except:
                    print "Ocurrio un error al intentar grabar"
                    break

        if options['importar_orientacion']:
            """
            Comando para importar tipo archivo
            """

            archivo = options['archivo']
            fileHandle = open(archivo)
            fileList = fileHandle.readlines()

            for fileLine in fileList:
                [orientacion_id, orientacion] = fileLine.split("|")
                orientacion = orientacion.strip(' \t\n\r')
                print orientacion_id, orientacion

                try:
                    # ojo para la imagen grabar de la siguinete manera image = 'image/'+image
                    orientacion = Orientacion(id=orientacion_id, orientacion=orientacion)
                    orientacion.save()

                except:
                    print "Ocurrio un error al intentar grabar"
                    break

        if options['importar_permisos']:
            """
            Comando para importar tipo archivo
            """

            archivo = options['archivo']
            fileHandle = open(archivo)
            fileList = fileHandle.readlines()

            for fileLine in fileList:
                [permisos_id, permisos] = fileLine.split("|")
                permisos = permisos.strip(' \t\n\r')
                print permisos_id, permisos

                try:
                    # ojo para la imagen grabar de la siguinete manera image = 'image/'+image
                    permisos = Permisos(id=permisos_id, permisos=permisos)
                    permisos.save()

                except:
                    print "Ocurrio un error al intentar grabar"
                    break

        if options['importar_perspectiva']:
            """
            Comando para importar tipo archivo
            """

            archivo = options['archivo']
            fileHandle = open(archivo)
            fileList = fileHandle.readlines()

            for fileLine in fileList:
                [perspectiva_id, perspectiva] = fileLine.split("|")
                perspectiva = perspectiva.strip(' \t\n\r')
                print perspectiva_id, perspectiva

                try:
                    # ojo para la imagen grabar de la siguinete manera image = 'image/'+image
                    perspectiva = Perspectiva(id=perspectiva_id, perspectiva=perspectiva)
                    perspectiva.save()

                except:
                    print "Ocurrio un error al intentar grabar"
                    break
