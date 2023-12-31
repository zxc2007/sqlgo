class SQlgoBasicException(Exception):
    pass

class SQLgoNoParameterFoundException(SQlgoBasicException):
    pass

class SQLgoWrongUrlException(SQlgoBasicException):
    pass