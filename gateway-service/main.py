# gateway-service/main.py
# API GATEWAY: unico punto de entrada al sistema (puerto 8000).
# Reenvia (proxy) cada peticion al microservicio correspondiente.

from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="API Gateway - FastBite")

# TODO 1: define un diccionario con la URL base de cada microservicio:
RUTAS = {
    "usuarios": "http://localhost:8001",
    "menu": "http://localhost:8002",
    "pedidos": "http://localhost:8003",
}

@app.api_route("/api/{servicio}/{ruta_resto:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def gateway(servicio: str, ruta_resto: str, request: Request):
    # TODO 2: valida que "servicio" exista en RUTAS; si no, retorna {"error": "servicio no encontrado"}

    # TODO 3: construye la url destino: f"{RUTAS[servicio]}/{ruta_resto}"

    # TODO 4: usando httpx.AsyncClient, reenvia la peticion con el mismo metodo HTTP
    # (request.method), y si tiene body, reenvialo tambien (await request.body())
    # Ejemplo:
    # async with httpx.AsyncClient() as client:
    #     respuesta = await client.request(request.method, url_destino, content=await request.body())
    # return respuesta.json()
    pass
