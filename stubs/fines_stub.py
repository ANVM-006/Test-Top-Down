class FinesStub:
    """Stub que simula el sistema de multas"""

    def tiene_multas(self, usuario_id):
        # STUB: Usuarios con ID múltiplo de 5 tienen multas
        return usuario_id % 5 == 0
