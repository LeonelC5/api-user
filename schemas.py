from pydantic import BaseModel
class Item(BaseModel):
    nombre: str
    apellido: str
    correo: str
    password: str
    celular: str
    description: str
    imagen: str
