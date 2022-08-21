import asyncio, models
from fastapi import APIRouter, Form, Cookie, status
from fastapi.responses import FileResponse, RedirectResponse
from twilio.rest import Client
from verify import Verification
from fastapi import APIRouter, Depends
import database, models
from sqlalchemy.orm import Session
from hashing import Hash


settings = models.Settings()

router = APIRouter(
    prefix=("/verification"),
    tags=['Verification']
)
client = Client(settings.twilio_account_sid, settings.twilio_auth_token)

@router.get('')
async def index():
    return FileResponse('html/index.html')

@router.post('')
async def handle_form(name: str = Form(),email: str = Form(), password: str = Form()):
    await asyncio.get_event_loop().run_in_executor(
        None, Verification.send_verification_code, email)
    response = RedirectResponse('/verify',
                                status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie('email', email)
    hashed = Hash.bcrypt(password)
    global new_email
    new_email = models.Users(email=email, name=name, password= hashed)
    return response

@router.get('/verify')
async def verify():
    return FileResponse('html/verify.html')

@router.post('/verify')
async def verify_code(db : Session = Depends(database.get_db),email: str = Cookie(None), code: str = Form(...)):
    verified = await asyncio.get_event_loop().run_in_executor(
        None, Verification.check_verification_code, email, code)
    if verified:
        db.add(new_email)
        db.commit()
        db.refresh(new_email)
        return RedirectResponse('/success',
                                status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse('/verify',
                                status_code=status.HTTP_303_SEE_OTHER)

@router.get('/success')
async def success():
    return FileResponse('html/success.html')
    