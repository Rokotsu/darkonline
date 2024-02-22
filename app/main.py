from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.crypto_rate.router import router as router_crypto
from app.sites.router import router as router_site


app = FastAPI()
app.include_router(router_crypto)
app.include_router(router_site)

# Подключение CORS, чтобы запросы к API могли приходить из браузера
origins = [
    "https://darkonion.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)