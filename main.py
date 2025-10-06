import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def get_response(apikey, messages):
    client = genai.Client(api_key=apikey)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages) # GenerateContentResponse object
    return response


def main():
    # Initialize
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not sys.argv[1]:
        print(Exception("Please provide a valid API key in the .env file or as a command line argument."))
        exit(1)
    user_prompt = sys.argv[1]
    is_verbose = False if len(sys.argv) < 3 else sys.argv[2] == "--verbose"
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    # Get response
    response = get_response(api_key, messages)

    # Show to user
    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
