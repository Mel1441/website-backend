#from curriculum.programs import router as curriculum_router
from models.ping import router as auth_router
#from forensic.dns_probe import router as dns_router
from app.routes.auth import router as login_router

def include_all_routes(app):
    app.include_router(auth_router, prefix="/models")
    app.include_router(login_router, prefix="/login")
    #pp.include_router(dns_router, prefix="/forensic")