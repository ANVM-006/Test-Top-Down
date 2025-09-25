class PaymentStub:
    """Stub que simula pagos de membresías"""
    def verificar_pago(self, usuario_id):
        # Solo los múltiplos de 3 están al día con el pago
        return usuario_id % 3 == 0
