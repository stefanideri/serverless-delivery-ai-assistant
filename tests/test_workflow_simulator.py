from delivery_ai_assistant.workflow_simulator import simulate_delivery_workflow


def _base_order(payment_status="approved"):
    return {
        "order_id": "PED-1001",
        "customer": {
            "name": "Thiago",
            "address": "Porto Alegre - RS",
            "phone": "+55 51 99999-9999",
        },
        "items": [{"name": "Pizza Calabresa", "quantity": 1, "price": 59.9}],
        "payment_status": payment_status,
    }


def test_approved_workflow():
    result = simulate_delivery_workflow(_base_order())

    assert result["status"] == "confirmed"
    assert result["bedrock_prompt"] is not None
    assert result["next_step"] == "Atualizar status para preparing"


def test_invalid_workflow():
    order = _base_order()
    order["items"] = []

    result = simulate_delivery_workflow(order)

    assert result["status"] == "invalid_order"
    assert result["bedrock_prompt"] is None
    assert "errors" in result


def test_declined_payment_workflow():
    result = simulate_delivery_workflow(_base_order("declined"))

    assert result["status"] == "payment_declined"
    assert result["next_step"] == "Solicitar novo pagamento"


def test_pending_payment_workflow():
    result = simulate_delivery_workflow(_base_order("pending"))

    assert result["status"] == "payment_pending"
    assert result["next_step"] == "Aguardar confirmação do pagamento"

