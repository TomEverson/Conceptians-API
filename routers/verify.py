import asyncio, models
from fastapi import APIRouter, Form, status
from fastapi.responses import RedirectResponse
from twilio.rest import Client
from verify import Verification
from fastapi import APIRouter, Depends
import database, models , schemas
from sqlalchemy.orm import Session
from hashing import Hash


settings = models.Settings()

router = APIRouter(
    prefix=("/verification"),
    tags=['Verification']
)
client = Client(settings.twilio_account_sid, settings.twilio_auth_token)

@router.post('')
async def handle_form(request: schemas.Verify):
    await asyncio.get_event_loop().run_in_executor(
        None, Verification.send_verification_code, request.email)
    response = RedirectResponse('verification/verify',
                                status_code=status.HTTP_303_SEE_OTHER)
    hashed = Hash.bcrypt(request.password)
    avatar = 'https://media.discordapp.net/attachments/987011683245522944/1011219957402587146/Screenshot_2022-08-22_at_4.56.57_PM.png?width=726&height=671'
    global new_email
    new_email = models.Users(email=request.email, name=request.name, password= hashed, avatar=avatar)
    return response

@router.get('/verify')
async def verify():
    confirm = "Confirm"
    return confirm

@router.post('/verify')
async def verify_code(request: schemas.CodeVerify,db : Session = Depends(database.get_db)):
    verified = await asyncio.get_event_loop().run_in_executor(
        None, Verification.check_verification_code, request.email, request.code)
    if verified:
        db.add(new_email)
        db.commit()
        db.refresh(new_email)
        return "Success"
    else:
        return RedirectResponse('/verify',
                                status_code=status.HTTP_303_SEE_OTHER)
