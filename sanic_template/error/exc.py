from sanic.exceptions import SanicException, add_status_code


@add_status_code(400)
class SQLOperationException(SanicException):
    pass
