from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.mako')
def my_view(request):
    return {'project': 'mako_play'}

@view_config(route_name='lesson1',renderer='templates/lesson1.mako')
def lesson1(request):
    return {'d': 4}

@view_config(route_name='lesson2',renderer='templates/lesson2.mako')
def lesson2(request):

    # hey folks, I swear my scraper only returns text so you do not need to
    # escape it!!
    scrapped_text = "   <a href='http://google.com/'>hi all</a>    "

    return {"show_this_text": scrapped_text}

@view_config(route_name='lesson3', renderer='templates/lesson3.mako')
def lesson3(request):
    return {"x": 40}

@view_config(route_name='lesson4', renderer='templates/lesson4.mako')
def lesson4(request):
    return {}

@view_config(route_name='lesson5', renderer='templates/lesson5.mako')
def lesson5(request):
    return {}

@view_config(route_name='lesson6', renderer='templates/lesson6.mako')
def lesson6(request):
    return {'my_view_var': 'hello'}

@view_config(route_name="lesson7", renderer ='templates/lesson7.mako')
def lesson7(request):
    return {}

@view_config(route_name="lesson8", renderer ='templates/lesson8/lesson8.mako')
def lesson8(request):
    return {}