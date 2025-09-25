class ReserveStub:
    """Stub que simula reservas de libros"""
    def reservar_libro(self, usuario_id, libro_id):
        print(f"[STUB] Reserva creada: Usuario={usuario_id}, Libro={libro_id}")
        return True
