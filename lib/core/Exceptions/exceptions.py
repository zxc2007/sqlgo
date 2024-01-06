class SQlgoBasicException(Exception):
    pass

class SQLgoNoParameterFoundException(SQlgoBasicException):
    pass

class SQLgoWrongUrlException(SQlgoBasicException):
    pass

class SQLgoNoneKeyException(SQlgoBasicException):
    pass

class SQLgoKeyGenDictKeyException(SQlgoBasicException):
    pass
