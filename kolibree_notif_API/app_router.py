# import random
import threading
from django.http import Http404
from django.conf import settings
from kolibree_notif_API.utils import get_header
from kolibree_notif_API import settings
from django.utils.deprecation import MiddlewareMixin


request_cfg = threading.local()


class RouterMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        client_id = get_header(request, "x_client_id")
        user_agent = get_header(request, "user_agent")
        if not client_id:
            request_cfg.db = 'default'
        elif int(client_id) in getattr(settings, 'COLGATE_CLIENT_ID'):
            request_cfg.db = 'colgate'
        else:
            request_cfg.db = 'default'
        request.db = request_cfg.db
        print(request.db)

    def process_response(self, request, response):
        if hasattr(request_cfg, 'db'):
            del request_cfg.db
        return response


class DatabaseRouter(object):
    def _default_db(self):
        if hasattr(request_cfg, 'db') and request_cfg.db == 'colgate':
            return 'colgate'
        else:
            return 'default'

    def db_for_read(self, model, **hints):
        #return random.choice([self._default_db(), self._default_db() + '_replica'])
        return self._default_db()

    def db_for_write(self, model, **hints):
        return self._default_db()

    def allow_relation(self, obj1, obj2, **hints):
        if self._default_db() == 'colgate':
            db_list = ('colgate')
        else:
            db_list = ('default')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_syncdb(self, db, model):
        if self._default_db() == 'colgate':
            db_list = ('colgate')
        else:
            db_list = ('default')

    def allow_migrate(self, db, app_label, model=None, **hints):
        if db == 'colgate':
            return db == 'colgate'
        else:
            return db == 'default'
