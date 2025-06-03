# Requisitos Funcionales

## Descripción General de la Aplicación

La aplicación es un sistema de librería online desarrollado en Django, dividido en dos módulos principales:
1. **App Catálogo**: Permite gestionar el inventario de libros, géneros, autores y proveedores; controla el stock disponible de cada libro.
2. **App Ventas**: Se encarga del flujo de compra de los clientes: mostrar catálogo para adquirir libros, gestionar un carrito de compras, procesar ventas (con estados de “En preparación”, “Cancelada”, “Enviada” y “Entregada”) y mantener el historial de transacciones.

Con esta estructura, los administradores pueden mantener actualizado el inventario y los usuarios registrados pueden navegar el catálogo, armar su carrito y completar pedidos con seguimiento de estados.

---

## Aplicación Catálogo

- **Gestión de Libros**  
  - Crear, leer, actualizar y eliminar libros con los siguientes campos:  
    - ISBN  
    - Título  
    - Autor (relación con entidad Autor)  
    - Género (relación con entidad Género)  
    - Precio  
    - Stock disponible  
    - Proveedor (relación con entidad Proveedor)

- **Gestión de Géneros**  
  - Crear, leer, actualizar y eliminar géneros literarios (p. ej. “Ficción”, “No ficción”, “Ciencia”).  
  - Asociar cada libro a uno o varios géneros.

- **Gestión de Autores**  
  - Crear, leer, actualizar y eliminar autores (nombre completo y datos de contacto).  
  - Asociar cada libro a uno o varios autores.

- **Gestión de Proveedores**  
  - Crear, leer, actualizar y eliminar proveedores (nombre, dirección, teléfono, email).  
  - Asociar cada libro a un proveedor responsable del stock.

- **Control de Stock**  
  - Al crear o editar un libro, asignar cantidad de stock inicial.  
  - Registrar entradas de stock a partir de los proveedores (opcionalmente: fecha y cantidad recibida).  
  - Consultar stock actual por libro y mostrar alerta o indicador si el stock cae por debajo de un nivel mínimo (definido en Catálogo).

- **Listado de Libros en Catálogo**  
  - Mostrar todos los libros disponibles en el catálogo, con filtros por género, autor y proveedor.  
  - Permitir ordenar por título, precio o stock.  
  - Paginación para navegación cuando hay muchos registros.

- **Detalle de Libro**  
  - Ver página individual de cada libro con información completa: título, autor(es), género(s), precio, stock disponible y datos del proveedor.  
  - Desde esta página, enlace rápido para editar o eliminar el libro (solo usuarios autorizados).

---

## Aplicación Ventas

- **Gestión de Clientes**  
  - Crear, leer, actualizar y eliminar clientes con datos:  
    - Nombre y apellido  
    - Correo electrónico  
    - Dirección de envío  
    - Teléfono de contacto  
  - Cada cliente debe tener un identificador único (p. ej. email).

- **Catálogo de Libros para Venta**  
  - Mostrar, para cualquier usuario (invitado o autenticado), la lista de libros disponibles para compra con:  
    - Título  
    - Autor(es)  
    - Género(s)  
    - Precio  
    - Stock disponible  
  - Indicar claramente cuándo un libro está agotado (stock = 0) y deshabilitar la opción de agregarlo al carrito.

- **Carrito de Compras**  
  - Permitir a un cliente (o usuario invitado) agregar uno o varios libros al carrito, especificando la cantidad deseada para cada libro.  
  - Verificar, al agregar, que la cantidad solicitada no exceda el stock disponible.  
  - Mostrar resumen del carrito con:  
    - Lista de ítems (libro, cantidad, precio unitario, subtotal)  
    - Total acumulado al día (sumatoria de subtotales)  
  - Permitir actualizar cantidades o eliminar ítems del carrito antes de finalizar la compra.

- **Flujo de Venta**  
  - Al confirmar el carrito, crear una entidad Venta con estado inicial **“En preparación”**.  
  - Estados posibles de la Venta:  
    1. **En preparación**: Cliente está completando detalles (dirección, método de pago, etc.).  
    2. **Cancelada**: Venta anulada por cliente o por administrador (stock devuelto si ya se descontó).  
    3. **Enviada**: Paquete despachado al cliente (stock debería descontarse al pasar a este estado).  
    4. **Entregada**: Cliente ha recibido la compra.  
  - Cada cambio de estado debe registrarse con fecha y usuario responsable del cambio.

- **Validación de Stock durante Venta**  
  - Antes de confirmar definitivamente una venta, verificar que para cada ítem la cantidad solicitada aún esté disponible en stock.  
  - Si el stock fue modificado (por otra venta o ajuste de inventario) y ya no alcanza, informar al cliente y permitir ajustar la cantidad o eliminar el ítem.  
  - Una vez confirmada la venta en estado “En preparación”, descontar el stock de todos los libros incluidos (o, alternativamente, descontar al pasar a “Enviada”).

- **Historial de Ventas**  
  - Mostrar listado de todas las ventas realizadas con filtros posibles por:  
    - Fecha de creación  
    - Cliente  
    - Estado (Preparación, Cancelada, Enviada, Entregada)  
  - Cada registro de venta debe incluir información mínima:  
    - Identificador de venta  
    - Cliente asociado  
    - Fecha de creación  
    - Estado actual  
    - Total de la venta

- **Detalle de Venta**  
  - Ver página individual de cada venta con:  
    - Datos del cliente (nombre, dirección, teléfono)  
    - Lista de ítems comprados (libro, cantidad, precio unitario, subtotal)  
    - Total final de la venta  
    - Historial de cambios de estado (fecha, estado anterior y nuevo estado, usuario que realizó el cambio)

- **Gestión de Estados de Venta**  
  - Administrador (o usuario con permisos) podrá cambiar el estado de una venta:  
    1. De **En preparación** a **Enviada** (stock previamente descontado)  
    2. De **Enviada** a **Entregada**  
    3. En cualquier momento, cambiar a **Cancelada** (si aún no está “Entregada”).  
  - Al cancelar una venta:  
    - Si el stock ya fue descontado, se debe reponer la cantidad correspondiente de cada libro.  
    - Registrar motivo de cancelación y usuario que la originó.

- **Carrito Persistente (Opcional)**  
  - Para clientes autenticados, mantener el contenido del carrito asociado a su cuenta, de modo que puedan retomar compras en sesiones futuras.  
  - Para usuarios invitados, almacenar temporalmente en sesión; si se registran antes de finalizar la venta, migrar carrito a su cuenta de cliente.

- **Notificación de Estado de Venta**  
  - Enviar correo electrónico automático al cliente cuando la venta cambie a “Enviada” o “Entregada”.  
  - Mostrar en el panel de cliente un historial de notificaciones con fechas y estado actual.

---
