from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from src.routes.routes_manager import RoutesManager

app = FastAPI(
    title="API - Joel Sigüenza",
    description="API con Arquitectura Hexagonal para Caso Práctico - Guinea Mobile",
    version="1.0.0"
)

# configuración de CORS
#! permitir todos los origenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# redirecciona a la documentacion
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

# rutas de endpoints
routes_manager = RoutesManager(app)
routes_manager.include_routes()