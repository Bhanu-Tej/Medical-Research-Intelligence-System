from fastapi import FastAPI

app = FastAPI(
    title="Medical Research Intelligence System"
)

@app.get("/")
def home():
    return {
        "message": "Medical Research Intelligence System Running"
    }