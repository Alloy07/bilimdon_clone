from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from jose import JWTError, jwt

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Request, HTTPException, Depends

from app.database import db_dep
from app.models import User
