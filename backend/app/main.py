from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Personal Knowledge Copilot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Welcome to Personal Knowledge Copilot API"}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
