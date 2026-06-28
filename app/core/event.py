from dataclasses import dataclass, field


@dataclass
class Event:

    text: str

    agents: list = field(default_factory=list)

    results: dict = field(default_factory=dict)