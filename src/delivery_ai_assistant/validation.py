from .models import Customer, DeliveryOrder, OrderItem, ValidationResult


VALID_PAYMENT_STATUSES = {"approved", "declined", "pending"}


def validate_customer(customer: Customer | None) -> list[str]:
    errors: list[str] = []

    if customer is None:
        return ["Cliente é obrigatório."]

    if not customer.name or not customer.name.strip():
        errors.append("Cliente precisa ter nome.")

    if not customer.address or not customer.address.strip():
        errors.append("Cliente precisa ter endereço.")

    return errors


def validate_items(items: list[OrderItem]) -> list[str]:
    errors: list[str] = []

    if not items:
        return ["Pedido precisa ter pelo menos um item."]

    for index, item in enumerate(items, start=1):
        if not item.name or not item.name.strip():
            errors.append(f"Item {index} precisa ter nome.")
        if item.quantity <= 0:
            errors.append(f"Item {index} precisa ter quantidade maior que zero.")
        if item.price < 0:
            errors.append(f"Item {index} não pode ter preço negativo.")

    return errors


def validate_payment_status(payment_status: str) -> list[str]:
    if payment_status not in VALID_PAYMENT_STATUSES:
        accepted = ", ".join(sorted(VALID_PAYMENT_STATUSES))
        return [f"payment_status inválido. Valores aceitos: {accepted}."]
    return []


def validate_order(order: DeliveryOrder) -> ValidationResult:
    errors = [
        *validate_customer(order.customer),
        *validate_items(order.items),
        *validate_payment_status(order.payment_status),
    ]
    return ValidationResult(is_valid=not errors, errors=errors)

