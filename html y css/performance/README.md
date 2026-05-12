🎸 Documentación: Landing Page – Shattered Riffs
📌 Resumen del Proyecto
El sitio web de Shattered Riffs es una landing page diseñada para proyectar una identidad visual cruda y enérgica. Se ha transformado la base inicial en una experiencia funcional que permite a los usuarios consultar fechas de gira, conocer la historia de la banda y visualizar contenido multimedia, todo bajo un entorno responsivo.

🏗️ Estructura HTML (Semántica)
Se ha seguido un flujo lógico utilizando etiquetas de HTML5 para mejorar el SEO y la accesibilidad.

Secciones Principales:
<header>: Contiene el logotipo de la banda, la navegación principal (<nav>) y un botón de clase .menu-toggle preparado para interactividad en dispositivos móviles.

<section class="hero">: El impacto visual inicial que utiliza una imagen de fondo de alto contraste y una llamada a la acción (CTA) para los eventos.

<section id="events">: Implementa una <table> para organizar las fechas de la gira, ciudades y sedes, proporcionando una lectura clara de los datos.

<section id="about">: Utiliza un contenedor de clase .about__content que divide el espacio entre una imagen representativa y un <article> con la biografía y una lista de influencias (<ul>).

<section id="media">: Una galería visual que utiliza una cuadrícula de imágenes para mostrar la estética de la banda.

<footer>: Incluye el cierre de copyright y una lista de redes sociales (social).

🎨 Guía de Estilos CSS
El diseño se basa en una paleta "Rock Style" oscura con acentos vibrantes.

Variables de Color (:root):
Primario: #1b6363 (Verde petróleo profundo para fondos de sección).

Secundario: #9e2424 (Rojo sangre para botones, encabezados de tabla y acentos).

Terciario: #0b0b0f (Negro carbón para el fondo general del cuerpo).

Técnicas de Layout:
Flexbox: Utilizado en el .header para la distribución del menú y en el .hero para el alineamiento vertical del contenido.

CSS Grid:

En la sección About, se aplica grid-template-columns: repeat(2, 1fr) para separar texto e imagen.

En la sección Media, se usa una cuadrícula de 3 columnas para la galería.

Efectos Visuales: Se implementó una transición de scale: 1.1 en el botón del Hero para mejorar la experiencia de usuario (Hover state).

📱 Diseño Responsivo (Media Queries)
El sitio ha sido optimizado para ofrecer una experiencia fluida en pantallas menores a 768px.

Ajustes en Móvil:
Tipografía: Reducción del tamaño de fuente base a 14px para mejorar la legibilidad en pantallas pequeñas.

Sección About: El layout cambia de dos columnas a una sola columna vertical (grid-template-columns: 100%), permitiendo que la imagen y el texto se apilen.

Galería Multimedia: La cuadrícula de imágenes se reajusta a 2 columnas en lugar de 3, evitando que las fotos se vean demasiado pequeñas.

Navegación: Se incluye el selector .menu-toggle para permitir (vía JS) el despliegue de un menú hamburguesa que ahorre espacio vertical.

🛠️ Organización de Activos
El proyecto mantiene una estructura de carpetas limpia para facilitar el mantenimiento:

/assets/css/style.css: Contiene toda la lógica visual organizada por secciones.

/assets/img/: Almacena las 10 imágenes de la banda y la guía de referencia.

/assets/js/main.js: Archivo destinado a la lógica del menú móvil y actualizaciones dinámicas (como el año en el footer).

🧠 Notas de Implementación
Tablas: Se utilizó border-collapse: collapse y bordes de color secundario para integrar la tabla de eventos con la estética general del sitio.

Imágenes: Se aplicó max-width: 100% de forma global para prevenir desbordamientos de contenedores en dispositivos móviles.

🔥 Shattered Riffs – Ready to Rock!
