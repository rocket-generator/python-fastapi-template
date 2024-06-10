class ServiceException(Exception):

    response_code: int = 500

    def __init__(self, *args, **kwargs):
        pass
