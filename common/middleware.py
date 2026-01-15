import uuid
from django.utils.deprecation import MiddlewareMixin


class RequestIdMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request_id = request.headers.get('x-request-id') or str(uuid.uuid4())
        request.request_id = request_id
        return None

    def process_response(self, request, response):
        request_id = getattr(request, 'request_id', None)
        if request_id:
            response['x-request-id'] = request_id
        return response
