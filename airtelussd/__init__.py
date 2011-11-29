from pyramid.config import Configurator
from pyramid.httpexceptions import (
    HTTPClientError,
    HTTPMethodNotAllowed)
from pyramid.view import view_config
from pyramid.response import Response
from airtelussd import templates


def request_requires(request, keys=[]):
    for key in keys:
        if key not in request.POST:
            raise HTTPClientError('Missing tag %s from request' % key)


options = [{'menu': 1, 'title': 'Check your blance'}]


def error(user_input):
    return Response(templates.error.render(user_input=user_input))


def index_menu(request, session_id, user_input):
    return Response(templates.index.render(menu=options))


@view_config(route_name='index')
def index(request):
    if request.method == 'POST':
        request_requires(request, keys=['SESSIONID', 'REQUESTNEW', 'INPUT'])
        session_id = request.POST.get('SESSIONID')
        request_new_p = request.POST.get('REQUESTNEW')
        user_input = request.POST.get('INPUT')
        if request_new_p == True:
            return index_menu(request, session_id, user_input)
        if user_input == '1':
            return index_menu(request, session_id, user_input)
        return error(user_input)
    else:
        return HTTPMethodNotAllowed()


def main(global_settings, **settings):
    config = Configurator(settings=settings)
    config.add_route('index', '/')
    config.scan()
    return config.make_wsgi_app()
