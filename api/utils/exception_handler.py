from rest_framework.views import exception_handler
from api.models import Logging

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        request = context['request']
        Logging.objects.create(
            endpoint=request.path,
            method=request.method,
            status_code=response.status_code,
            error_message=str(exc)
        )

    return response