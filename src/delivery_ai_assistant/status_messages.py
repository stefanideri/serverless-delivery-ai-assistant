STATUS_MESSAGES = {
    "confirmed": "Pedido confirmado e enviado para preparação.",
    "invalid_order": "Pedido inválido. Revise os dados informados antes de tentar novamente.",
    "payment_declined": "Pagamento recusado. Solicite outro método de pagamento.",
    "payment_pending": "Pagamento pendente. Aguarde a confirmação antes de preparar o pedido.",
    "preparing": "Pedido em preparação.",
    "out_for_delivery": "Pedido saiu para entrega.",
    "delivered": "Pedido entregue com sucesso.",
}


def get_status_message(status: str) -> str:
    return STATUS_MESSAGES.get(status, "Status desconhecido.")

