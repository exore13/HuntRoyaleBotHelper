from typing import List
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()
expectedCharactersArraySize = 19

class WebFormData(BaseModel):
    speed: int
    text: str
    characters: List[int]

# Endpoint al cual se le envia la seleccion de personajes, la velocidad y otra variable ne formato de texto
@app.post("/webInterfaceInfo")
async def recibir_datos(request: Request):
    print("Endpoint /webInterfaceInfo was invoked")
    datos_json = await request.json()
    if len(datos_json['characters']) != expectedCharactersArraySize:
        return JSONResponse(content={"error": "Characters array invalid size"}, status_code=400)
    if fail_if_repeated_id(datos_json['characters']):
        return JSONResponse(content={"error": "Characters array should not have repeated IDs"}, status_code=400)

    print("Speed: ", datos_json['speed'])
    print("Text: ", datos_json['text'])
    print("Characters: ", datos_json['characters'])
    for id in datos_json['characters']:
        print(id)

### Endpoints que se encargan de ejecutar los ficheros script
@app.get("/dragon")
async def dragon():
    print("Endpoint /dragon was invoked")
    exec(open('./scripts/dragon.py').read())

@app.get("/kraken")
async def kraken():
    print("Endpoint /kraken was invoked")
    exec(open('./scripts/kraken.py').read())

@app.get("/yeti")
async def yeti():
    print("Endpoint /yeti was invoked")
    exec(open('./scripts/yeti.py').read())
###

### Funcion auxiliar
def fail_if_repeated_id(list):
    if len(list) == len(set(list)):
        return False
    return True
### 

## API Startup || Con esta linea, la api se enciende sola al ejecutar el fichero `py api.py`
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=47359)
