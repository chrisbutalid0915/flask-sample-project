import logging
from app.config import Config
from passlib.context import CryptContext
from werkzeug.exceptions import NotFound

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    user = db.query.filter(db.username==username).first()
    if user is None:
        logging.error(f"User not found")
        raise NotFound('User not found')
    return user


def authtenticate_user(db, username: str, password: str):
    # check if the user exist
    user = get_user(db, username)
    if not user:
        return False
    # verify the user's password
    if not verify_password(password, user.password_hash):
        return False
    return user