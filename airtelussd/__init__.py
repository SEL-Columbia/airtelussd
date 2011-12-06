from pyramid.config import Configurator
from pyramid.httpexceptions import (
    HTTPClientError,
    HTTPMethodNotAllowed)
from pyramid.view import view_config
from pyramid.response import Response
from airtelussd import templates


options = (('A', 'Add power time'),
           ('B', 'Check Balance'),
           ('C', 'Turn Circuit On'),
           ('D', 'Turn Circuit Off'),
           ('E', 'Check 30 Day Status'),
           ('F', 'Change contact number'),
           ('G', 'Meter mission'), )


def error(user_input):
    return Response(templates.error.render(user_input=user_input))


def index_menu(request, session_id, user_input):
    """
    Function to render the main SharedSolar USSD index.
    """
    return Response(templates.index.render(menu=options), headerslist=[''])


def check_balance(request, session_id, user_input):
    """
    Allows user to check their balance.
    """


@view_config(route_name='index')
def index(request):
    """
    Main view function that displays all of the USSD options This view
    function checks to make sure that Airtel gives us the correct
    request keys, or tags (The term used by the Airtel Tech).
    """
    if request.method == 'POST':
        session_id = request.POST.get('SESSIONID')
        # check that we have the required keys
        if session_id is None:
            raise HTTPClientError('Missing session id')
        request_new_p = request.POST.get('REQUESTNEW')  # this is a guess
        if request_new_p is None:
            raise HTTPClientError('Missing new requrest tag')
        user_input = request.POST.get('INPUT')  # this is also a guess
        if user_input is None:
            raise HTTPClientError('Missing user input tag')

        return Response(user_input)
    else:
        return HTTPMethodNotAllowed()


def main(global_settings, **settings):
    config = Configurator(settings=settings)
    config.add_route('index', '/')
    config.scan()
    return config.make_wsgi_app()
