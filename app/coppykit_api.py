from fastapi import FastAPI, HTTPException, Depends, Query
from coppykit import generate_branding_snippet, generate_branding_keywords
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

MAX_USER_INPUT_LENGTH = int(os.getenv('USER_INPUT_MAX_LENGTH', 50))

class BrandingResponse(BaseModel):
    snippet: Optional[str]
    keywords: List[str]
    

app = FastAPI()

def validate_prompt_length(prompt: str = Query(...)) -> str:
    print(prompt)
    if len(prompt) > MAX_USER_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input length is too long. Must be under {MAX_USER_INPUT_LENGTH}"
        )
    return prompt

@app.get("/generate_snippet", response_model=BrandingResponse)
@validate_prompt_length
async def generate_snippet(prompt: str = Depends(validate_prompt_length)):
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}

@app.get("/generate_keywords", response_model=BrandingResponse)
@validate_prompt_length
async def generate_keywords(prompt: str = Depends(validate_prompt_length)):
    keywords = generate_branding_keywords(prompt)
    return {"snippet": None, "keywords": keywords}

@app.get("/generate_snippet_and_keywords", response_model=BrandingResponse)
@validate_prompt_length
async def generate_snippet_and_keywords(prompt: str = Depends(validate_prompt_length)):
    snippet = generate_branding_snippet(prompt)
    keywords = generate_branding_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}
