from fastapi import FastAPI
from dundie.db import ActiveSession

app = FastAPI(
    title="dundie",
    version="0.1.0",
    description="dundie is a rewards API",
)


from dundie.models import User
from sqlmodel import Session, select
from dundie.models.user import UserResponse


@app.get("/", response_model=UserResponse)
def hello(session: Session = ActiveSession):
    return session.exec(select(User)).first
