from .models import Users
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.postgresql.connection import engine
from sqlalchemy.exc import IntegrityError



class ManageUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    async def create(self):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                user = Users(
                    username=self.username,
                    password=self.password
                )
                session.add(user)
                try:
                    session.commit()
                except IntegrityError:
                    raise IntegrityError
                
    async def check(self):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                user = await session.execute(select(Users).order_by(Users.username==self.username).limit(1))
                user = user.scalar_one_or_none()
                return user
            



async def check_cookie(session_id, username, active_users):
    accurate_cookie = active_users[username]
    if session_id == accurate_cookie["session_id"]:
        return True
    else: return False
    