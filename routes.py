#from curriculum.programs import router as curriculum_router
from models.ping import router as auth_router
#from forensic.dns_probe import router as dns_router

def include_all_routes(app):
    app.include_router(auth_router, prefix="/models")
    #app.include_router(curriculum_router, prefix="/curriculum")
    #pp.include_router(dns_router, prefix="/forensic")