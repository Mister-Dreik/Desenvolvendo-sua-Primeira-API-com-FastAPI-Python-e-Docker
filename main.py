from fastapi import FastAPI
from fastapi_pagination import add_pagination

app = FastAPI()

# Importa e registra os endpoints relacionados aos atletas
from atletas import router as atletas_router
app.include_router(atletas_router)

# Configuração da paginação global
add_pagination(app)
