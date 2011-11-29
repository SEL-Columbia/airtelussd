from pyramid.config import Configurator
from pyramid.httpexceptions import (
    HTTPClientError,
    HTTPMethodNotAllowed)

from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='index_menu')
def index_menu(request):
    if request.method == 'POST':
        session_id = request.POST.get('SESSIONID')
        if session_id is None:
            HTTPClientError()
        request_new_p = request.POST.get('REQUESTNEW')
        if request_new_p is None:
            HTTPClientError()
        user_input = request.POST.get('INPUT')
        if user_input is None:
            HTTPClientError()
        return Response()
    else:
        return HTTPMethodNotAllowed()


def main(global_settings, **settings):
    config = Configurator(settings=settings)
    config.add_route('index_menu', '/')
    config.scan()
    return config.make_wsgi_app()
