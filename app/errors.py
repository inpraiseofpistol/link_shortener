class HandlingError(Exception):
    def __init__(self, *args, status: int = 400):
        super().__init__(*args)
        self.status = status

class UserAlreadyExists(HandlingError): pass
class LinkNotFound(HandlingError):
    def __init__(self, *args):
        super().__init__(*args, status=404)