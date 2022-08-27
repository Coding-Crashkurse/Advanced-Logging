import uvicorn
from fastapi import FastAPI
from customlogging import logging_config

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_config=logging_config)
