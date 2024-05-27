import uvicorn
from fastapi import FastAPI
from contas.routers import contas_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/programador")
def oi_eu_sou_programador() -> str:
    return "Oi, eu sou um programador!"

app.include_router(contas_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
