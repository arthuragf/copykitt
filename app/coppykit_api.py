from fastapi import FastAPI, Query
from coppykit import generate_branding_snippet, generate_branding_keywords
from pydantic import BaseModel
from typing import List, Optional, Annotated
import os
from dotenv import load_dotenv
from mangum import Mangum

load_dotenv()

MAX_USER_INPUT_LENGTH = int(os.getenv('USER_INPUT_MAX_LENGTH', 32))
MIN_USER_INPUT_LENGTH = int(os.getenv('USER_INPUT_MIN_LENGTH', 3))


class BrandingResponse(BaseModel):
    snippet: Optional[str]
    keywords: List[str]
    

app = FastAPI()
handler = Mangum(app)


@app.get("/generate_snippet", response_model=BrandingResponse)
async def generate_snippet(
        prompt: Annotated[
            str, 
            Query(..., max_length=MAX_USER_INPUT_LENGTH, min_length=MIN_USER_INPUT_LENGTH)
        ]
):
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}


@app.get("/generate_keywords", response_model=BrandingResponse)
async def generate_keywords(
        prompt: Annotated[
            str, 
            Query(..., max_length=MAX_USER_INPUT_LENGTH, min_length=MIN_USER_INPUT_LENGTH)
        ]
):
    keywords = generate_branding_keywords(prompt)
    return {"snippet": None, "keywords": keywords}


@app.get("/generate_snippet_and_keywords", response_model=BrandingResponse)
async def generate_snippet_and_keywords(
        prompt: Annotated[
            str, 
            Query(..., max_length=MAX_USER_INPUT_LENGTH, min_length=MIN_USER_INPUT_LENGTH)
        ]
):
    snippet = generate_branding_snippet(prompt)
    keywords = generate_branding_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}
