from typing import Union

from fastapi import Body, FastAPI, Response, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from schemas import Skills, LinkResponse, MessageBody
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

@app.get("/online-me")
def social():
    return {"Linkedin": "https://www.linkedin.com/in/akhil-pulimala/",
            "github": "https://github.com/akhilpulimala"}

@app.get("/resume", response_model=LinkResponse)
def view_resume():
    return {"link": "https://yellow-stacia-24.tiiny.site"}

@app.get("/contact-me")
def contact_me():
    return {"mobile": "8129490391",
            "email": "akhilpulimala@gmail.com"}

@app.post("/text-me/")
async def text_me_now(your_name: str,
                      number: str,
                      content: MessageBody):
    
    return {f"Hi {your_name}, Thanks for reaching out , Will getback you soon"}
