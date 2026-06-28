from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:

    amount: int

    transaction_type: str

    category: str

    description: str

    created_at: datetime