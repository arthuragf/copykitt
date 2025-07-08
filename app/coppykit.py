import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'package'))

from google import genai
from google.genai import types
from dotenv import load_dotenv
from typing import List
import argparse
import json
load_dotenv()

MAX_USER_INPUT_LENGTH = int(os.getenv('USER_INPUT_MAX_LENGTH', 50))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    if validate_prompt_length(user_input):
        generate_branding_snippet(user_input)
        generate_branding_keywords(user_input)
    else:
        raise ValueError(f"Input length is too long. Must be lower than {MAX_USER_INPUT_LENGTH}")


def validate_prompt_length(prompt:str) -> bool:
    return len(prompt) <= MAX_USER_INPUT_LENGTH


def generate_branding_snippet(prompt:str) -> str:
    enriched_prompt = f"Generate upbeat branding snippet for {prompt}"
    system_instructions = "return the result on the text key of the JSON"
    response = make_ai_request(enriched_prompt, system_instructions)
    response = json.loads(response.text)["text"].strip()
    print(f"snippet: {response}")
    return response


def generate_branding_keywords(prompt:str) -> List[str]:
    enriched_prompt = f"Generate key words for this branding: {prompt}"
    system_instructions = "return the keywords separated by , on the keywords key of the JSON"
    response = make_ai_request(enriched_prompt, system_instructions)
    keywords = [keyword.lower() for keyword in json.loads(response.text)['keywords'].strip().split(",")]
    print(f"keywords: {keywords}")
    return keywords 


def make_ai_request(prompt:str, system_instruction:str="") -> types.GenerateContentResponse:
    client = genai.Client()
    gemini_response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            temperature=0.6,
            response_mime_type="application/json",
            system_instruction=system_instruction
        ),
        contents=prompt
    )
    
    return gemini_response


if __name__ == '__main__':
    main()