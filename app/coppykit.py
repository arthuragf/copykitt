from google import genai
from google.genai import types
from dotenv import load_dotenv
import argparse
import json
load_dotenv()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print(generate_branding_snippet(user_input))
    print(generate_branding_keywords(user_input))


def generate_branding_snippet(prompt:str) -> str:
    enriched_prompt = f"Generate upbeat branding snippet for {prompt}"
    system_instructions = "return the result on the text key of the JSON"
    response = make_ai_request(enriched_prompt, system_instructions)
    
    return json.loads(response.text)["text"].strip()


def generate_branding_keywords(prompt:str) -> str:
    enriched_prompt = (f"Generate key words for this branding: {prompt}")
    system_instructions = "return the keywords separated by , on the keywords key of the JSON"
    response = make_ai_request(enriched_prompt, system_instructions)
    
    return json.loads(response.text)['keywords'].strip()


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