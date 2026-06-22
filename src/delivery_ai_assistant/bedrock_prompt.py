from .models import DeliveryOrder


def build_customer_message_prompt(order: DeliveryOrder, status: str) -> str:
    customer_name = order.customer.name if order.customer else "cliente"
    item_names = ", ".join(item.name for item in order.items) or "itens do pedido"

    return (
        "Gere uma mensagem curta, clara e amigável em português para o cliente "
        f"{customer_name}, informando que o pedido {order.order_id} com {item_names} "
        f"está com o status '{status}'. A mensagem deve ser adequada para um "
        "assistente de delivery e não deve incluir dados sensíveis."
    )

