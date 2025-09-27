from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import auth, schemas

router = APIRouter()

@router.post("/admin/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not auth.authenticate_admin(form_data.username, form_data.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = auth.create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}