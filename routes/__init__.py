from .sql_injection import init_routes as sql_injection_routes
from .xss import init_routes as xss_routes
from .upload import init_routes as upload_routes
from .csrf import init_routes as csrf_routes
from .idor import init_routes as idor_routes

def register_routes(app):
    sql_injection_routes(app)
    xss_routes(app)
    upload_routes(app)
    csrf_routes(app)
    idor_routes(app)
