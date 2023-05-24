from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/test")
async def test(websocket: WebSocket):
    await websocket.accept()
    raise RuntimeError("failed")
