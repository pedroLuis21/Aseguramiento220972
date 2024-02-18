class SistemaReservas:
    def __init__(self):
        self.reservas = {}
        self.next_id = 1

    def reservar_habitacion(self, habitacion, fecha_inicio, fecha_fin, nombre_cliente):
        reserva_id = self.next_id
        self.reservas[reserva_id] = {
            'habitacion': habitacion,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'nombre_cliente': nombre_cliente
        }
        self.next_id += 1
        return reserva_id

    def eliminar_reserva(self, reserva_id):
        if reserva_id in self.reservas:
            del self.reservas[reserva_id]

    def obtener_reserva(self, reserva_id):
        return self.reservas.get(reserva_id)
