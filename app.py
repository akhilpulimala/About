from typing import Union

from fastapi import FastAPI, Response, Request
from fastapi.responses import HTMLResponse
from schemas import Skills, LinkResponse
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def welcome(request: Request):

   root_url = request.url_for("welcome")
   return f"""
    <html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
       To know more about me, come through the back door!! <a href='{root_url}docs'>open</a>
    </html>
    """


@app.get("/about")
def about():
    return {"I am a seasoned backend developer with over 5 years of experience. My expertise lies in developing robust and scalable backend solutions using technologies such as FastAPI, SQLAlchemy, and PostgreSQL. I also have experience in integrating machine learning components into backend systems, allowing for advanced data processing and analysis capabilities."}

@app.get("/skills")
def skills():
    return Skills.skills

@app.get("/onlineme", response_model=LinkResponse)
def social():
    return {"link": "https://www.linkedin.com/in/akhil-pulimala/"}
