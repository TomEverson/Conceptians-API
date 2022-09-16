import asyncio, models
from fastapi import APIRouter, Form, status
from fastapi.responses import RedirectResponse
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

@router.post('')
async def handle_form(name: str = Form(),email: str = Form(), password: str = Form()):
    await asyncio.get_event_loop().run_in_executor(
        None, Verification.send_verification_code, email)
    response = RedirectResponse('verification/verify',
                                status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie('email', email)
    hashed = Hash.bcrypt(password)
    rabbit = "https://cdn.discordapp.com/attachments/987011683245522944/1011219957402587146/Screenshot_2022-08-22_at_4.56.57_PM.png"
    global new_email
    new_email = models.Users(email=email, name=name, password= hashed, avatar = rabbit)
    return response

@router.get('/verify')
async def verify():
    confirm = "Confirm"
    return confirm

@router.post('/verify')
async def verify_code(db : Session = Depends(database.get_db),email: str = Form(...), code: str = Form(...)):
    verified = await asyncio.get_event_loop().run_in_executor(
        None, Verification.check_verification_code, email, code)
    if verified:
        db.add(new_email)
        db.commit()
        db.refresh(new_email)
        return "Success"
    else:
        return RedirectResponse('/verify',
                                status_code=status.HTTP_303_SEE_OTHER)
