# ESTE ARCHIVO SE AGREGA/INTEGRA AL orders-service YA EXISTENTE (Semana 3)
# Implementa CQRS (separa comandos de consultas) + Event Sourcing (el estado
# se reconstruye a partir de eventos, no se guarda directamente).

# TODO 1: crea una lista global "event_store = []" que sera el almacen de eventos

event_store = []

def comando_crear_pedido(usuario: str, items: list):
    """
    LADO DEL COMANDO (escritura).
    En vez de guardar el pedido final directamente, se guarda un EVENTO.
    """
    # TODO 2: crea el evento como dict:
    # {"tipo": "PedidoCreado", "datos": {"usuario": usuario, "items": items}}
    # TODO 3: agregalo a event_store
    # TODO 4: retorna una confirmacion simple, ej: {"status": "evento registrado"}
    pass

def comando_cancelar_pedido(pedido_id: int):
    """Otro comando: agrega un evento PedidoCancelado."""
    # TODO 5: agrega el evento {"tipo": "PedidoCancelado", "datos": {"pedido_id": pedido_id}}
    pass

def consulta_resumen_pedidos():
    """
    LADO DE LA CONSULTA (lectura).
    Reconstruye el estado actual RECORRIENDO (replaying) todos los eventos guardados.
    Este modelo de lectura es DISTINTO a como se guardaron los datos.
    """
    resumen = []
    # TODO 6: recorre event_store; por cada evento tipo "PedidoCreado", agrega
    # un pedido a "resumen"; por cada "PedidoCancelado", marca ese pedido como cancelado
    # (esto es una version simplificada de "replay" de eventos)
    return resumen
