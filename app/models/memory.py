from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Memory:

    text: str

    created_at: datetime

    source: str = "user"

    importance: int = 3

    entities: list = field(default_factory=list)

    tags: list = field(default_factory=list)

    action: str = ""

    category: str = ""

    follow_up: bool = False