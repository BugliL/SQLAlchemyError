from dataclasses import dataclass, field


@dataclass
class B:
    description: str
    value_y: str
    id_b: int = field(default=None)
