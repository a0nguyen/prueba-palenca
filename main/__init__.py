from functools import lru_cache
from fastapi.responses import JSONResponse

from fastapi import FastAPI, Request, Depends
class CustomHTTPException(Exception):
    def __init__(self, status_code: int, body: dict):
        self.status_code = status_code
        self.body = body

class AbortWithJson:
    @staticmethod
    def call(code: int, body: dict):
        raise CustomHTTPException(
            status_code=code,
            body=body
        )

app = FastAPI()


@app.post('/uber/login')
async def get_profile(request: Request):
    body = await request.json()
    print('body:', body)
    if body.get('email') == 'pierre@palenca.com' and body.get('password') == 'MyPwdChingon123':
        return  {
            'message': 'SUCCESS',
            'access_token': 'cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5'
        }
    else:
        AbortWithJson.call(401, {
            'message': 'CREDENTIALS_INVALID',
            'details': 'Incorrect username or password'
        })


@app.post('/uber/get-profile')
async def get_profile(request: Request):
    body = await request.json()
    if body.get('access_token') != 'cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5':
        AbortWithJson.call(401, {
            'message': 'CREDENTIALS_INVALID',
            'details': 'Incorrect token'
        })
    else:
        return  {
            'message': 'SUCCESS',
            'access_token': 'cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5'
        }


@app.exception_handler(CustomHTTPException)
async def custom_http_exception_handler(request: Request, exc: CustomHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.body
    )
