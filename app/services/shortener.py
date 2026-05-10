import string
import random

class ShortenerService:
    def generate_code(self) -> str:
        chars = string.ascii_letters + string.digits
        return "".join(random.choices(chars, k=6))