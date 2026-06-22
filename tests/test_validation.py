from delivery_ai_assistant.models import Customer, DeliveryOrder, OrderItem
from delivery_ai_assistant.validation import validate_order


def test_valid_order():
    order = DeliveryOrder(
        order_id="PED-1001",
        customer=Customer(name="Thiago", address="Porto Alegre - RS"),
        items=[OrderItem(name="Pizza", quantity=1, price=59.9)],
        payment_status="approved",
    )

    result = validate_order(order)

    assert result.is_valid is True
    assert result.errors == []


def test_order_without_customer():
    order = DeliveryOrder(
        order_id="PED-1002",
        customer=None,
        items=[OrderItem(name="Pizza", quantity=1, price=59.9)],
        payment_status="approved",
    )

    result = validate_order(order)

    assert result.is_valid is False
    assert "Cliente é obrigatório." in result.errors


def test_order_without_items():
    order = DeliveryOrder(
        order_id="PED-1003",
        customer=Customer(name="Thiago", address="Porto Alegre - RS"),
        items=[],
        payment_status="approved",
    )

    result = validate_order(order)

    assert result.is_valid is False
    assert "Pedido precisa ter pelo menos um item." in result.errors


def test_item_with_zero_quantity():
    order = DeliveryOrder(
        order_id="PED-1004",
        customer=Customer(name="Thiago", address="Porto Alegre - RS"),
        items=[OrderItem(name="Pizza", quantity=0, price=59.9)],
        payment_status="approved",
    )

    result = validate_order(order)

    assert result.is_valid is False
    assert "Item 1 precisa ter quantidade maior que zero." in result.errors


def test_invalid_payment_status():
    order = DeliveryOrder(
        order_id="PED-1005",
        customer=Customer(name="Thiago", address="Porto Alegre - RS"),
        items=[OrderItem(name="Pizza", quantity=1, price=59.9)],
        payment_status="canceled",
    )

    result = validate_order(order)

    assert result.is_valid is False
    assert any("payment_status inválido" in error for error in result.errors)

