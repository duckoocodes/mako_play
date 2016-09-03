from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.mako')
def my_view(request):
    return {'project': 'mako_play'}

@view_config(route_name='lesson1',renderer='templates/lesson1.mako')
def lesson1(request):
    return {'my_variable': 'this is my very first mako'}