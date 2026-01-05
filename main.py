import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("API Key Invalid (is it missing?)")
    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="Custom Bot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages, # <- the custom argument that can be changed
    )

    usage = response.usage_metadata
    if usage.prompt_token_count is None:
        raise RuntimeError("API Request failed. Please try again.")
    if args.verbose is True:
        print("User prompt:", args.user_prompt)
        print("Prompt tokens:", usage.prompt_token_count, "\nResponse tokens:", usage.candidates_token_count)
        print("Response:", response.text)

    else:
        print("Response:", response.text)

if __name__ == "__main__":
    main()
