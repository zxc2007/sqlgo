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

class SQLGOBeepSoundException(SQlgoBasicException):
    pass

class SQLGOStreamHandlerException(SQlgoBasicException):
    pass

class SQLGOFilePathException(SQlgoBasicException):
    pass

class SQLGOConnectionException(SQlgoBasicException):
    pass

class SQLGODataException(SQlgoBasicException):
    pass
