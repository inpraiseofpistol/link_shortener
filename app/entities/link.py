from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Link:
    id: int = field(default=None, init=False)
    original_url: str
    short_code: str
    user_id: int
    created_at: datetime = field(init=False, default_factory=lambda: datetime.now(timezone.utc))