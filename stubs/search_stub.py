class SearchStub:
    """Stub que simula búsqueda de libros"""
    def buscar_libro(self, titulo):
        # Simula búsqueda: títulos que contienen 'python' existen
        return "python" in titulo.lower()
