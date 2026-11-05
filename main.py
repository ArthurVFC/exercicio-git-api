from fastapi import FastAPI

# Cria a aplicação da API
app = FastAPI()

# Endpoint para verificar se a API está funcionando
@app.get("/health")
def health():
    return {"status": "ok", "origem": "feature"}

# Endpoint para consultar a versão da API
@app.get("/version")
def version():
    return "1.1.0"