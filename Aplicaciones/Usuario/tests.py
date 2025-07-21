from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.hashers import make_password, check_password
from django.db import models  # Importa models de Django
from Aplicaciones.Usuario.models import Usuario
from Aplicaciones.Administrador.models import Administrador
from Aplicaciones.Publicaciones.models import Propiedad
from unittest.mock import patch

# En Aplicaciones/Usuario/tests.py
class PropiedadTest(models.Model):
    titulo = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # Solo los campos absolutamente necesarios
    
    class Meta:
        app_label = 'Usuario'  # Para evitar migraciones
class UsuarioViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        # Crear un usuario de prueba
        self.usuario = Usuario.objects.create(
            usuario='testuser',
            correo='test@example.com',
            contrasena='hashedpassword',  # En realidad debería estar hasheada
            telefono='1234567890'
        )
        # Crear un admin de prueba
        self.admin = Administrador.objects.create(
            user='adminuser',
            passwo='adminpassword'  # Debería estar hasheada
        )

    def test_index_view(self):
        try:
            url = reverse('index')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'index.html')
            print("[✔] Prueba 'test_index_view' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_index_view'.")
            raise

    def test_inicio_view(self):
        try:
            url = reverse('inicios')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'inicios.html')
            print("[✔] Prueba 'test_inicio_view' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_inicio_view'.")
            raise

    def test_nuevo_usuario_view(self):
        try:
            url = reverse('nuevoUsuario')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'nuevoUsuario.html')
            print("[✔] Prueba 'test_nuevo_usuario_view' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_nuevo_usuario_view'.")
            raise

    def test_guardar_registro_post(self):
        try:
            url = reverse('guardaregistro')
            data = {
                'usuario': 'newuser',
                'correo': 'new@example.com',
                'contrasena': 'newpassword',
                'telefono': '9876543210'
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 302)
            self.assertTrue(Usuario.objects.filter(usuario='newuser').exists())
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), "¡Usuario registrado exitosamente!")
            print("[✔] Prueba 'test_guardar_registro_post' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_guardar_registro_post'.")
            raise

    def test_guardar_registro_duplicado_usuario(self):
        try:
            url = reverse('guardaregistro')
            data = {
                'usuario': 'testuser',  # Usuario ya existe
                'correo': 'new2@example.com',
                'contrasena': 'password',
                'telefono': '1234567890'
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 302)  # Redirección por error
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), "El nombre de usuario ya está en uso.")
            print("[✔] Prueba 'test_guardar_registro_duplicado_usuario' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_guardar_registro_duplicado_usuario'.")
            raise

    def test_guardar_registro_duplicado_correo(self):
        try:
            url = reverse('guardaregistro')
            data = {
                'usuario': 'newuser2',
                'correo': 'test@example.com',  # Correo ya existe
                'contrasena': 'password',
                'telefono': '1234567890'
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 302)  # Redirección por error
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), "El correo ya está registrado.")
            print("[✔] Prueba 'test_guardar_registro_duplicado_correo' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_guardar_registro_duplicado_correo'.")
            raise

    def test_iniciosesion_view_get(self):
        try:
            url = reverse('iniciosesion')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'iniciosesion.html')
            print("[✔] Prueba 'test_iniciosesion_view_get' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_iniciosesion_view_get'.")
            raise

    def test_iniciosesion_usuario_correcto(self):
        try:
            # Necesitamos un usuario con contraseña hasheada
            password = 'testpassword'
            hashed_pwd = make_password(password)
            usuario = Usuario.objects.create(
                usuario='loginuser',
                correo='login@example.com',
                contrasena=hashed_pwd,
                telefono='1234567890'
            )
            
            url = reverse('iniciosesion')
            data = {
                'usuario': 'loginuser',
                'contrasena': password
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 302)  # Redirección exitosa
            self.assertEqual(response.url, reverse('inicios'))
            
            # Verificar que la sesión se creó
            session = self.client.session
            self.assertEqual(session['usuario_id'], usuario.id)
            self.assertEqual(session['usuario_nombre'], usuario.usuario)
            
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), "¡Bienvenido!")
            print("[✔] Prueba 'test_iniciosesion_usuario_correcto' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_iniciosesion_usuario_correcto'.")
            raise

    def test_iniciosesion_usuario_incorrecto(self):
        try:
            url = reverse('iniciosesion')
            data = {
                'usuario': 'usuarioinexistente',
                'contrasena': 'password'
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 200)  # No redirecciona, muestra error
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), "El usuario no existe.")
            print("[✔] Prueba 'test_iniciosesion_usuario_incorrecto' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_iniciosesion_usuario_incorrecto'.")
            raise

    def test_iniciosesion_contrasena_incorrecta(self):
        try:
            url = reverse('iniciosesion')
            data = {
                'usuario': 'testuser',
                'contrasena': 'contrasenaincorrecta'
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 200)  # No redirecciona, muestra error
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), "Contraseña incorrecta.")
            print("[✔] Prueba 'test_iniciosesion_contrasena_incorrecta' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_iniciosesion_contrasena_incorrecta'.")
            raise

    def test_iniciosesion_admin_correcto(self):
        try:
            # Necesitamos un admin con contraseña hasheada
            password = 'adminpass'
            hashed_pwd = make_password(password)
            admin = Administrador.objects.create(
                user='adminlogin',
                passwo=hashed_pwd
            )
            
            url = reverse('iniciosesion')
            data = {
                'usuario': 'adminlogin',
                'contrasena': password
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 302)  # Redirección exitosa
            self.assertEqual(response.url, reverse('admiin'))
            
            # Verificar que la sesión se creó
            session = self.client.session
            self.assertEqual(session['admin_id'], admin.id)
            
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), "¡Bienvenido!")
            print("[✔] Prueba 'test_iniciosesion_admin_correcto' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_iniciosesion_admin_correcto'.")
            raise

    def test_cerrarsesion(self):
        try:
            # Primero iniciamos sesión
            session = self.client.session
            session['usuario_id'] = self.usuario.id
            session.save()
            
            url = reverse('cerrarsesion')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)  # Redirección
            self.assertEqual(response.url, reverse('iniciosesion'))
            
            # Verificar que la sesión se cerró
            self.assertNotIn('usuario_id', self.client.session)
            
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), "Sesión cerrada correctamente.")
            print("[✔] Prueba 'test_cerrarsesion' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_cerrarsesion'.")
            raise

    def test_perfil_usuario_get(self):
        try:
            # Primero iniciamos sesión
            session = self.client.session
            session['usuario_id'] = self.usuario.id
            session.save()
            
            url = reverse('perfil_usuario')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'perfil.html')
            self.assertContains(response, self.usuario.usuario)
            print("[✔] Prueba 'test_perfil_usuario_get' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_perfil_usuario_get'.")
            raise

    def test_perfil_usuario_post(self):
        try:
            # Primero iniciamos sesión
            session = self.client.session
            session['usuario_id'] = self.usuario.id
            session.save()
            
            url = reverse('perfil_usuario')
            data = {
                'usuario': 'usuarioactualizado',
                'correo': 'nuevo@example.com',
                'telefono': '9876543210',
                'contrasena': 'nuevacontrasena'
            }
            response = self.client.post(url, data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['success'], True)
            
            # Verificar que los datos se actualizaron
            self.usuario.refresh_from_db()
            self.assertEqual(self.usuario.usuario, 'usuarioactualizado')
            self.assertEqual(self.usuario.correo, 'nuevo@example.com')
            self.assertEqual(self.usuario.telefono, '9876543210')
            self.assertTrue(check_password('nuevacontrasena', self.usuario.contrasena))
            print("[✔] Prueba 'test_perfil_usuario_post' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_perfil_usuario_post'.")
            raise

    def test_perfil_usuario_sin_sesion(self):
        try:
            url = reverse('perfil_usuario')
            response = self.client.get(url)
            # Debería redirigir o devolver un error 401 según tu implementación
            # En tu código actual devuelve JsonResponse con error 401
            self.assertEqual(response.status_code, 401)
            print("[✔] Prueba 'test_perfil_usuario_sin_sesion' completada exitosamente.")
        except AssertionError:
            print("[✘] Error en la prueba 'test_perfil_usuario_sin_sesion'.")
            raise

    def test_detalle_propiedad_view(self):
        try:
            # Necesitamos crear un archivo temporal para la imagen
            from django.core.files.uploadedfile import SimpleUploadedFile
            import os
            
            # Crear una imagen temporal para la prueba
            from io import BytesIO
            from PIL import Image
            image = Image.new('RGB', (100, 100))
            image_file = BytesIO()
            image.save(image_file, 'JPEG')
            image_file.seek(0)
            
            propiedad = Propiedad.objects.create(
                titulo='Casa de prueba',
                imagen=SimpleUploadedFile(
                    name='test_image.jpg',
                    content=image_file.read(),
                    content_type='image/jpeg'
                ),
                descripcion='Descripción de prueba',
                precio=100000.00,
                ubicacion='Bogotá, Colombia',
                usuario=self.usuario,
                latitud=4.710989,
                longitud=-74.072090,
                estado='Disponible'
                # fecha_publicacion y fecha_actualizacion se llenan automáticamente
            )
            
            url = reverse('publicacion', args=[propiedad.id_propiedad])
            response = self.client.get(url)
            
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'publicacion.html')
            self.assertContains(response, 'Casa de prueba')
            
            # Limpiar el archivo temporal después de la prueba
            if os.path.exists(propiedad.imagen.path):
                os.remove(propiedad.imagen.path)
                
            print("[✔] Prueba 'test_detalle_propiedad_view' completada exitosamente.")
        except Exception as e:
            print(f"[✘] Error en la prueba 'test_detalle_propiedad_view': {str(e)}")
            raise