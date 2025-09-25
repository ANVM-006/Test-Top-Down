from biblioteca_sistema import BibliotecaSistema
from stubs.database_stub import DatabaseStub
from stubs.auth_stub import AuthStub
from stubs.notification_stub import NotificationStub
from stubs.fines_stub import FinesStub
from stubs.recommendation_stub import RecommendationStub
from stubs.logging_stub import LoggingStub
from stubs.payment_stub import PaymentStub
from stubs.search_stub import SearchStub
from stubs.reserve_stub import ReserveStub
from stubs.analytics_stub import AnalyticsStub

def crear_sistema():
    return BibliotecaSistema(
        db=DatabaseStub(),
        auth=AuthStub(),
        notification=NotificationStub(),
        fines=FinesStub(),
        recommendation=RecommendationStub(),
        logging=LoggingStub(),
        payment=PaymentStub(),
        search=SearchStub(),
        reserve=ReserveStub(),
        analytics=AnalyticsStub()
    )

def test_pago_membresia_pendiente():
    sistema = crear_sistema()
    resultado = sistema.prestar_libro(usuario_id=1, libro_id=2)  # 1 no es múltiplo de 3
    assert resultado == "Pago de membresía pendiente"

def test_prestamo_registra_analitica_y_log():
    sistema = crear_sistema()
    resultado = sistema.prestar_libro(usuario_id=3, libro_id=2)  # válido
    assert resultado == "Préstamo exitoso"

def test_recomendacion_usuario_par():
    sistema = crear_sistema()
    recomendacion = sistema.recomendar_libro(usuario_id=2)
    assert recomendacion == "Libro A"

def test_recomendacion_usuario_impar():
    sistema = crear_sistema()
    recomendacion = sistema.recomendar_libro(usuario_id=1)
    assert recomendacion == "Libro B"

def test_busqueda_libro_existente():
    sistema = crear_sistema()
    assert sistema.buscar_libro("Python avanzado") is True

def test_busqueda_libro_inexistente():
    sistema = crear_sistema()
    assert sistema.buscar_libro("Historia del arte") is False

def test_reserva_libro():
    sistema = crear_sistema()
    resultado = sistema.reservar_libro(usuario_id=4, libro_id=10)
    assert resultado is True
