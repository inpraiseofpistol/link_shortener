import string
import random
from app.repositories.link import LinkRepository

class ShortenerService:
    def __init__(self, link_repo: LinkRepository):
        self.link_repo = link_repo

    async def generate_unique_code(self) -> str:
        chars = string.ascii_letters + string.digits
        while True:
            code = "".join(random.choices(chars, k=6))
            if not await self.link_repo.get_by_code(code):
                return code