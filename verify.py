import asyncio
from twilio.rest import Client
import models

settings = models.Settings()

client = Client(settings.twilio_account_sid, settings.twilio_auth_token)

class Verification():
    def send_verification_code(email):
        verification = client.verify.services(
        settings.twilio_verify_service).verifications.create(
            to=email, channel='email')
        assert verification.status == 'pending'

    def check_verification_code(email, code):
        verification = client.verify.services(
        settings.twilio_verify_service).verification_checks.create(
            to=email, code=code)
        return verification.status == 'approved'