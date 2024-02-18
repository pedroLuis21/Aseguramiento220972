import pytest
from reservas import SistemaReservas

@pytest.fixture
def sistema_reservas():
    return SistemaReservas()

def test_eliminar_reserva(sistema_reservas):
    # Agregar una reserva de prueba
    reserva_id = sistema_reservas.reservar_habitacion('101', '2024-02-17', '2024-02-19', 'Juan Perez')
    
    # Verificar que la reserva fue agregada correctamente
    assert sistema_reservas.obtener_reserva(reserva_id) is not None
    
    # Eliminar la reserva
    sistema_reservas.eliminar_reserva(reserva_id)
    
    # Verificar que la reserva fue eliminada correctamente
    assert sistema_reservas.obtener_reserva(reserva_id) is None

def test_crear_reserva(sistema_reservas):
    # Crear una reserva nueva
    reserva_id = sistema_reservas.reservar_habitacion('102', '2024-02-20', '2024-02-22', 'Maria Garcia')
    
    # Verificar que la reserva fue agregada correctamente
    assert sistema_reservas.obtener_reserva(reserva_id) is not None
