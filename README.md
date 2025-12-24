# Mi Primera Página - Arquitectura Residencial

Portafolio web profesional de arquitectura con galería de proyectos y carga de archivos.

⚠️ **PROYECTO EN DESARROLLO** - Esta es una versión inicial con funcionalidades básicas. Se añadirán más características próximamente.

## Características
- Diseño responsivo (funciona en móvil, tablet y escritorio)
- Galería de proyectos con banner
- Carga y descarga de archivos
- Formulario de contacto
- Tema profesional oscuro

## Uso Local
1. Asegúrate de tener Python 3.7+
2. Ejecuta `run_server.bat`
3. Abre `http://localhost:8000` en tu navegador

## Desplegar en Railway
1. Ve a [railway.app](https://railway.app)
2. Haz clic en "New Project"
3. Selecciona "Deploy from GitHub" o "Deploy from Repo"
4. Sube esta carpeta
5. Railway automáticamente detectará `Procfile` y ejecutará tu servidor
6. Obtendrás una URL pública como `https://tuproyecto.railway.app`

## ⏳ Pendiente por Implementar
- [ ] Galería de imágenes en banner (actualmente muestra placeholder)
- [ ] Carrusel de proyectos destacados
- [ ] Filtrado de archivos por categoría
- [ ] Sistema de usuarios/login
- [ ] Base de datos para persistencia (actualmente local)
- [ ] Optimización de imágenes
- [ ] Integración con redes sociales
- [ ] Chat en vivo de soporte

## Archivos principales
- `index.html` - Página de inicio
- `proyectos.html` - Galería y carga de archivos
- `estilos.css` - Estilos profesionales
- `script.js` - Interactividad
- `server_upload.py` - Backend Python
