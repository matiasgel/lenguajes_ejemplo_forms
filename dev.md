# Documentación de Desarrollo

## Desarrollo Realizado

### Aplicación Catálogo
- Se creó la aplicación `catalogo`.
- Se implementaron los modelos:
  - `Autor`: Para gestionar autores.
  - `Genero`: Para gestionar géneros literarios.
  - `Proveedor`: Para gestionar proveedores.
  - `Libro`: Para gestionar libros, incluyendo relaciones con autores, géneros y proveedores.
- Se generó un archivo de fixtures (`catalogo_fixture.json`) con datos iniciales.

### Aplicación Ventas
- Se creó la aplicación `ventas`.
- Se implementaron los modelos:
  - `Cliente`: Para gestionar información de clientes.
  - `Venta`: Para gestionar el flujo de ventas y sus estados.
  - `ItemVenta`: Para gestionar los ítems de cada venta.
- Se creó una vista en la aplicación `ventas` para mostrar todos los libros disponibles como una tienda.
- La vista utiliza el modelo `Libro` de la aplicación `catalogo` para listar los libros con stock disponible.
- Se implementó un template modular (`store.html`) utilizando Bootstrap para mostrar los libros con detalles como título, autor(es), género(s), precio y stock.
- Se agregó una ruta en `urls.py` para acceder a la tienda de libros en `/store/`.

### Plantilla Base
- Se creó una plantilla base (`base.html`) con un diseño moderno que incluye un header y footer.
- La plantilla utiliza Bootstrap para garantizar una experiencia de usuario óptima.

### Mejora de la Tienda de Libros
- Se actualizó el diseño de la tienda de libros (`store.html`) para incluir imágenes y enlaces a los detalles de cada libro.
- La vista ahora utiliza un diseño moderno con Bootstrap para mejorar la experiencia del usuario.

## Tareas Pendientes

### Aplicación Catálogo
- Implementar vistas y formularios para CRUD de libros, autores, géneros y proveedores.
- Crear lógica para alertas de stock bajo.
- Implementar filtros y paginación en el listado de libros.
- Crear vistas detalladas para cada libro.

### Aplicación Ventas
- Implementar vistas y formularios para CRUD de clientes.
- Crear lógica para el flujo de ventas y validación de stock.
- Implementar carrito de compras persistente.
- Crear lógica para notificaciones automáticas por correo electrónico.
- Implementar historial de ventas con filtros.
- Implementar funcionalidad para agregar libros al carrito desde la tienda.
- Crear vistas para gestionar el carrito de compras.
- Configurar pruebas unitarias para la vista y el template de la tienda.

### General
- Configurar URLs y vistas iniciales para ambas aplicaciones.
- Realizar pruebas unitarias para los modelos creados.
- Documentar el código y agregar comentarios en los modelos y vistas.
- Configurar el entorno de desarrollo para pruebas locales.

## Integración de Aplicaciones y Base de Datos

### Integración de Aplicaciones
- Se agregaron las aplicaciones `catalogo` y `ventas` al archivo `settings.py` del proyecto Django.
- Las aplicaciones están ahora registradas en `INSTALLED_APPS`.

### Creación de la Base de Datos
- Se generaron las migraciones iniciales para las aplicaciones `catalogo` y `ventas`.
- Se aplicaron las migraciones para crear la estructura de la base de datos.
- La base de datos ahora incluye las tablas necesarias para gestionar libros, autores, géneros, proveedores, clientes, ventas y sus ítems.

### Integración de Bootstrap
- Se instaló el paquete `django-bootstrap4` para integrar Bootstrap en el proyecto.
- Se agregó `bootstrap4` a la lista de aplicaciones en `INSTALLED_APPS` dentro de `settings.py`.
- Ahora ambas aplicaciones (`catalogo` y `ventas`) pueden utilizar estilos y componentes de Bootstrap para mejorar la interfaz de usuario.

### Paginación y Filtros en la Tienda de Libros
- Se agregó lógica de paginación en la vista `store_view` para mostrar 12 libros por página.
- Se implementaron filtros de búsqueda por título y género en la tienda.
- El template `store.html` fue actualizado para incluir un formulario de búsqueda y controles de paginación.
- La tienda ahora permite a los usuarios buscar libros de manera más eficiente y navegar entre páginas.

### Changes to Views

#### StoreView
- Converted `store_view` to a class-based view using `ListView`.
- Added filtering logic for `query` and `autor` parameters.
- Implemented pagination with 12 items per page.
- Context includes `query` and `autor` for use in templates.

#### BookDetailView
- Converted `book_detail_view` to a class-based view using `DetailView`.
- Displays detailed information about a single book.
- Context includes the `libro` object for use in templates.

### Próximos Pasos
- Poblar la base de datos con los fixtures creados (`catalogo_fixture.json` y `ventas_fixture.json`).
- Implementar vistas y formularios para las operaciones CRUD.
- Configurar URLs para las aplicaciones.
- Realizar pruebas unitarias para verificar la funcionalidad de los modelos y la base de datos.
- Continuar con la implementación de lógica de negocio y funcionalidades descritas en el `readme.md`.
- Implementar plantillas HTML utilizando Bootstrap para las vistas de ambas aplicaciones.
- Configurar formularios y vistas para aprovechar los estilos de Bootstrap.
- Realizar pruebas de diseño para garantizar una experiencia de usuario óptima.
- Implementar funcionalidad para agregar libros al carrito desde la vista de detalles.
- Crear vistas para gestionar el carrito de compras.
- Realizar pruebas unitarias para las vistas y templates creados.
- Continuar con la implementación de lógica de negocio y funcionalidades descritas en el `readme.md`.

---
