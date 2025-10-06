import os
import sys
from dotenv import load_dotenv
from google import genai


def get_response(apikey, prompt):
    client = genai.Client(api_key=apikey)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt) # GenerateContentResponse object
    return response


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not sys.argv[1]:
        print(Exception("Please provide a valid API key in the .env file or as a command line argument."))
        exit(1)
    prompt = sys.argv[1]

    response = get_response(api_key, prompt)
    print(response.text)

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
