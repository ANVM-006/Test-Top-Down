class NotificationStub:
    """Stub que simula notificaciones a los usuarios"""

    def enviar_notificacion(self, usuario_id, mensaje):
        # Simula envío de notificación
        print(f"[STUB] Notificación enviada a Usuario {usuario_id}: {mensaje}")
        return True
