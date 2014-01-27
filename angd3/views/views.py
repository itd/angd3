import collections
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )


######################################################
class BaseViews(object):
    """
    """

    def __init__(self, request):
        self.request = request
        renderer = get_renderer("../templates/layout.pt")
        self.layout = renderer.implementation().macros['layout']

    # @view_config(route_name='cdupowerdata_json',
    #              renderer='json')
    # def cdudata_json(self):
    #     dat = getcdupower(HP_CDUS)
    #     dat = collections.OrderedDict(sorted(dat.items()))

    #     return dat


    @view_config(route_name='home', renderer='templates/home.pt')
    def my_view(request):
        try:
            one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
        except DBAPIError:
            return Response(conn_err_msg, content_type='text/plain', status_int=500)
        return {'one': one, 'project': 'angd3'}
            @view_config(route_name='tbd_view', renderer='../templates/tbd.pt')

    def tbd_view(request):
        return {"title": 'To Be developed',
                "description": "This still needs to be done. Bug Kurt.",
        }


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_angd3_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

