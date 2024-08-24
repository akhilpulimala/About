import yaml
from typing import List
from pydantic import BaseModel, HttpUrl

with open('./skills.yaml', 'r') as file:
    data = yaml.safe_load(file)

class Skills:
    skills: List[str] = data['skills']

class LinkResponse(BaseModel):
    link: HttpUrl