from fastapi import FastAPI, Query
from coppykit import generate_branding_snippet, generate_branding_keywords
from pydantic import BaseModel
from typing import List, Optional, Annotated
import os
from dotenv import load_dotenv

load_dotenv()

MAX_USER_INPUT_LENGTH = int(os.getenv('USER_INPUT_MAX_LENGTH', 50))

class BrandingResponse(BaseModel):
    snippet: Optional[str]
    keywords: List[str]
    

app = FastAPI()

@app.get("/generate_snippet", response_model=BrandingResponse)
async def generate_snippet(prompt: Annotated[str, Query(..., max_length=32, min_length=3)]):
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}

@app.get("/generate_keywords", response_model=BrandingResponse)
async def generate_keywords(prompt: Annotated[str, Query(..., max_length=32, min_length=3)]):
    keywords = generate_branding_keywords(prompt)
    return {"snippet": None, "keywords": keywords}

@app.get("/generate_snippet_and_keywords", response_model=BrandingResponse)
async def generate_snippet_and_keywords(prompt: Annotated[str, Query(..., max_length=32, min_length=3)]):
    snippet = generate_branding_snippet(prompt)
    keywords = generate_branding_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}
