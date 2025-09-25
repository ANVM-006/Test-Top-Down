class BibliotecaSistema:
    def __init__(self, db, auth, notification=None, fines=None, recommendation=None,
                 logging=None, payment=None, search=None, reserve=None, analytics=None):
        self.db = db
        self.auth = auth
        self.notification = notification
        self.fines = fines
        self.recommendation = recommendation
        self.logging = logging
        self.payment = payment
        self.search = search
        self.reserve = reserve
        self.analytics = analytics

    def prestar_libro(self, usuario_id, libro_id):
        if not self.auth.verificar_usuario(usuario_id):
            return "Usuario no autorizado"

        if self.fines and self.fines.tiene_multas(usuario_id):
            return "Usuario con multas pendientes"

        if self.payment and not self.payment.verificar_pago(usuario_id):
            return "Pago de membresía pendiente"

        if not self.db.libro_disponible(libro_id):
            return "Libro no disponible"

        self.db.registrar_prestamo(usuario_id, libro_id)

        if self.notification:
            self.notification.enviar_notificacion(usuario_id, "Préstamo exitoso")

        if self.logging:
            self.logging.registrar_evento(f"Préstamo realizado por {usuario_id}")

        if self.analytics:
            self.analytics.registrar_uso("préstamo_libro")

        return "Préstamo exitoso"

    def recomendar_libro(self, usuario_id):
        if self.recommendation:
            return self.recommendation.recomendar_libro(usuario_id)
        return None

    def buscar_libro(self, titulo):
        if self.search:
            return self.search.buscar_libro(titulo)
        return False

    def reservar_libro(self, usuario_id, libro_id):
        if self.reserve:
            return self.reserve.reservar_libro(usuario_id, libro_id)
        return False
