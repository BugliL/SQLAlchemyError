from dataclasses import dataclass, field

@dataclass
class B:
    description: str
    value_y: bool
    id_b: int = field(default=None)
  
