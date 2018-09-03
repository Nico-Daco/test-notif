from django.http import HttpResponse
# import requests
from rest_framework.renderers import JSONRenderer

def get_header(request, name):
    """
    test different headers. For instance, is name="x_client_id", get_header will test in the following order:
    http_x_client_id, x_client_id, http_http_x_client_id
    HTTP_X_CLIENT_ID, X_CLIENT_ID, HTTP_HTTP_X_CLIENT_ID
    """
    import os
    string_ = "http_"+name
    if request.META.get(string_):
        return request.META.get(string_)
    string_ = name
    if request.META.get(string_):
        return request.META.get(string_)
    string_ = "http_http_"+name
    if request.META.get(string_):
        return request.META.get(string_)
    string_ = "http_"+name
    if request.META.get(string_.upper()):
        return request.META.get(string_.upper())
    string_ = name
    if request.META.get(string_.upper()):
        return request.META.get(string_.upper())
    string_ = "http_http_"+name
    if request.META.get(string_.upper()):
        return request.META.get(string_.upper())
    string_ = "HTTP_" + name
    if os.environ.get(string_.upper()):
        return os.environ[string_.upper()]
    return None

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
