from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('lesson1', '/lesson1')
    config.add_route('lesson2', '/lesson2')
    config.add_route('lesson3', '/lesson3')
    config.add_route('lesson4', '/lesson4')
    config.add_route('lesson5', '/lesson5')
    config.add_route('lesson6', '/lesson6')
    config.scan()
    return config.make_wsgi_app()
