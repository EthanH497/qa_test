from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controllers import user_router

app = FastAPI()

# Allow cross origin access
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# User Router
app.include_router(user_router)


@app.get(f'/health/check')
def root():
    return {"message": "Service is healthy"}
