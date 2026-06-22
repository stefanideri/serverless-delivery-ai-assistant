from dataclasses import dataclass, field


@dataclass(frozen=True)
class Customer:
    name: str
    address: str
    phone: str = ""


@dataclass(frozen=True)
class OrderItem:
    name: str
    quantity: int
    price: float


@dataclass(frozen=True)
class DeliveryOrder:
    order_id: str
    customer: Customer | None
    items: list[OrderItem] = field(default_factory=list)
    payment_status: str = "pending"


@dataclass(frozen=True)
class WorkflowResult:
    order_id: str
    status: str
    message: str
    next_step: str
    bedrock_prompt: str | None = None
    errors: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ValidationResult:
    is_valid: bool
    errors: list[str] = field(default_factory=list)

