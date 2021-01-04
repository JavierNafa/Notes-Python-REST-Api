class ResponseError(Exception):

    def __init__(self, code=400, data=None, message=''):
        self.status = code
        self.data = data
        self.message = message
