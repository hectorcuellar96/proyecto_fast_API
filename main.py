from fastapi import FastAPI
from routers.products import router as  products_router

app = FastAPI()

app.include_router(products_router)

@app.get("/")
def home():
  return {"mensaje":"Hola Mundo"}