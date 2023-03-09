Dependencias
- fastapi
- uvicorn

```
    pip install "uvicorn[standard]"
    pip install fastapi
```

---

He probado la API haciendo una llamada POST /webInterfaceInfo con el siguiente payload.
*Primero he modificado la linea 8 del fichero, donde indicamos el tamaño del Array de IDs a esperar. Para esta prueba ponlo a 4*
```
{
    "speed": "42",
    "text": "Cadena de texto no entiendo bien para que",
    "characters": [10, 20, 30, 12]
}
```

