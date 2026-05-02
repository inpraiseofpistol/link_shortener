from dataclasses import dataclass, field

@dataclass
class User:
    id: int = field(default=None, init=False)
    email: str
    password_hash: str

