Sistema de Biblioteca – Testing Top Down con Stubs

Este proyecto implementa un ejercicio práctico de pruebas Top Down en un sistema de gestión de biblioteca.
La idea es simular módulos aún no implementados mediante stubs, permitiendo realizar pruebas tempranas de integración sin necesidad de que todo el sistema esté terminado.

Se implementaron 10 stubs diferentes, cada uno representando un módulo del sistema:

DatabaseStub -----> simula disponibilidad y registro de préstamos.

AuthStub -----> simula autenticación de usuarios.

NotificationStub -----> simula envío de notificaciones.

FinesStub -----> simula verificación de multas.

RecommendationStub -----> simula recomendaciones personalizadas de libros.

LoggingStub -----> simula registro de eventos en logs.

PaymentStub -----> simula verificación de pago de membresía.

SearchStub -----> simula búsqueda de libros.

ReserveStub -----> simula reserva de libros.

AnalyticsStub -----> simula registro de métricas de uso del sistema.

Estructura del Proyecto:

proyecto_biblioteca/
├── biblioteca_sistema.py     # Sistema principal (usa inyección de dependencias)
├── test_top_down.py          # Pruebas unitarias con pytest
└── stubs/                    # Carpeta con stubs simulados
    ├── __init__.py
    ├── database_stub.py
    ├── auth_stub.py
    ├── notification_stub.py
    ├── fines_stub.py
    ├── recommendation_stub.py
    ├── logging_stub.py
    ├── payment_stub.py
    ├── search_stub.py
    ├── reserve_stub.py
    └── analytics_stub.py


Instalación y Ejecución
1. Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

2. Instalar dependencias
pip install pytest

3. Ejecutar pruebas
pytest test_top_down.py -v --tb=short


Resultado esperado:

<img width="1528" height="254" alt="image" src="https://github.com/user-attachments/assets/c37ea1c3-e5bf-4073-aeca-9f4417b3fd04" />

Análisis de Ventajas del Testing Top Down con Stubs
🔹 1. Pruebas tempranas

Permite validar la lógica principal del sistema incluso si varios módulos aún no están implementados.

Se detectan errores antes de que el proyecto esté completo.

🔹 2. Reducción de dependencias

Los stubs aíslan el sistema de componentes externos (BD real, pagos, servicios externos).

Evita bloqueos en el desarrollo al no depender de servicios aún no listos.

🔹 3. Desarrollo paralelo

Distintos equipos pueden trabajar en paralelo: unos crean la lógica principal mientras otros implementan los módulos reales.

Los stubs sirven como contratos de interacción.

🔹 4. Pruebas controladas

Los stubs permiten definir condiciones específicas (ej: usuario con multas, pago pendiente, libro no disponible).

Se pueden generar casos de prueba difíciles de reproducir en un entorno real.

🔹 5. Documentación viva

Cada stub describe la intención de un módulo futuro.

Facilita la planificación y comunicación entre desarrolladores y testers.

🔹 6. Flexibilidad

Los stubs se reemplazarán fácilmente por implementaciones reales sin necesidad de modificar las pruebas.

Se garantiza que la integración posterior sea más sencilla.
