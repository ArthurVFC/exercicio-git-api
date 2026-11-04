from fastapi import FastAPI

# Cria a aplicação da API
app = FastAPI()

# Endpoint para verificar se a API está funcionando
@app.get("/health")
def health():
    return {"status": "ok"}