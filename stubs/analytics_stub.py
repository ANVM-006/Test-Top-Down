class AnalyticsStub:
    """Stub que simula analítica del sistema"""
    def registrar_uso(self, accion):
        print(f"[STUB] Analítica registrada: {accion}")
        return True
