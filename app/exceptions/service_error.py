class ServiceError(Exception):

    response_code: int = 500

    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.response_code = status_code
        super().__init__(self.message)
