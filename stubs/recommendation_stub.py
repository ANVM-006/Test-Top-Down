class RecommendationStub:
    """Stub que simula recomendaciones de libros"""
    def recomendar_libro(self, usuario_id):
        # Usuarios pares reciben recomendación de "Libro A", impares "Libro B"
        return "Libro A" if usuario_id % 2 == 0 else "Libro B"
