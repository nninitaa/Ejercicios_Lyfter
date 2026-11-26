class NotFoundError(Exception):
    """El recurso solicitado no existe (404)."""


class CarNotAvailableError(Exception):
    """El carro existe pero no está disponible para alquilar (409)."""
