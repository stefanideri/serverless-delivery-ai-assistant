from typing import Any

from .bedrock_prompt import build_customer_message_prompt
from .models import Customer, DeliveryOrder, OrderItem, WorkflowResult
from .status_messages import get_status_message
from .validation import validate_order


def _parse_order(order_data: dict[str, Any]) -> DeliveryOrder:
    customer_data = order_data.get("customer")
    customer = None
    if isinstance(customer_data, dict):
        customer = Customer(
            name=str(customer_data.get("name", "")),
            address=str(customer_data.get("address", "")),
            phone=str(customer_data.get("phone", "")),
        )

    items = [
        OrderItem(
            name=str(item.get("name", "")),
            quantity=int(item.get("quantity", 0)),
            price=float(item.get("price", 0)),
        )
        for item in order_data.get("items", [])
        if isinstance(item, dict)
    ]

    return DeliveryOrder(
        order_id=str(order_data.get("order_id", "UNKNOWN")),
        customer=customer,
        items=items,
        payment_status=str(order_data.get("payment_status", "")),
    )


def _result_to_dict(result: WorkflowResult) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "order_id": result.order_id,
        "status": result.status,
        "message": result.message,
        "bedrock_prompt": result.bedrock_prompt,
        "next_step": result.next_step,
    }
    if result.errors:
        payload["errors"] = result.errors
    return payload


def simulate_delivery_workflow(order_data: dict[str, Any]) -> dict[str, Any]:
    order = _parse_order(order_data)
    validation_result = validate_order(order)

    if not validation_result.is_valid:
        return _result_to_dict(
            WorkflowResult(
                order_id=order.order_id,
                status="invalid_order",
                message=get_status_message("invalid_order"),
                bedrock_prompt=None,
                next_step="Corrigir dados do pedido",
                errors=validation_result.errors,
            )
        )

    if order.payment_status == "declined":
        return _result_to_dict(
            WorkflowResult(
                order_id=order.order_id,
                status="payment_declined",
                message=get_status_message("payment_declined"),
                bedrock_prompt=None,
                next_step="Solicitar novo pagamento",
            )
        )

    if order.payment_status == "pending":
        return _result_to_dict(
            WorkflowResult(
                order_id=order.order_id,
                status="payment_pending",
                message=get_status_message("payment_pending"),
                bedrock_prompt=None,
                next_step="Aguardar confirmação do pagamento",
            )
        )

    status = "confirmed"
    bedrock_prompt = build_customer_message_prompt(order, status)
    customer_name = order.customer.name if order.customer else "cliente"
    message = (
        f"Olá, {customer_name}! Seu pedido {order.order_id} foi confirmado "
        "e já está em preparação. Avisaremos quando sair para entrega."
    )

    return _result_to_dict(
        WorkflowResult(
            order_id=order.order_id,
            status=status,
            message=message,
            bedrock_prompt=bedrock_prompt,
            next_step="Atualizar status para preparing",
        )
    )

