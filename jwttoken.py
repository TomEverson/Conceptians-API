from datetime import timedelta , datetime
from jose import JWTError, jwt
import schemas , database

get_db = database.get_db

JWT_KEY = "your_jwt_key"
REFRESH_KEY = 'your_refresh_key'
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, REFRESH_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
    # decode token and extract username and expires data
        payload = jwt.decode(token, JWT_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        id: str = payload.get("id")
        expires = payload.get("exp")
        token_data = schemas.TokenData(email=email, expires=expires)
    except JWTError:
        raise credentials_exception
    # validate username
    if email is None:
        raise credentials_exception
    # check token expiration
    if expires is None:
        raise credentials_exception
    if datetime.now().timestamp() > token_data.expires.timestamp():
        return "Token Expired"
    
    return id

    
def verify_refresh_token(token: str):
    payload = jwt.decode(token, REFRESH_KEY, algorithms=[ALGORITHM])
    if not payload:
        return "Error"
    email:str = payload.get("email")
    return email
    