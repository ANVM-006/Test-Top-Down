class LoggingStub:
    """Stub que simula logs del sistema"""
    def registrar_evento(self, evento):
        print(f"[STUB] Log registrado: {evento}")
        return True
