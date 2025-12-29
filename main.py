import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Load in env variables
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("API Key Invalid (is it missing?)")
    
    client = genai.Client(api_key=api_key)

    # Accept user input for prompts
    parser = argparse.ArgumentParser(description="Custom Bot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Store a list of messages
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Fetch the response from gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages, # <- the custom argument that can be changed
    )

    # Keep track of token usage
    usage = response.usage_metadata

    if usage.prompt_token_count is None:
        raise RuntimeError("API Request failed. Please try again.")
    
    # Check if the user included the --verbose flag
    if args.verbose is True:
        print("User prompt:", args.user_prompt)

        # Check how many tokens we're using
        print("Prompt tokens:", usage.prompt_token_count, "\nResponse tokens:", usage.candidates_token_count)

        # Print the models response to the cli
        print("Response:", response.text)

    else:
        # Print just the response if --verbose is NOT included
        print("Response:", response.text)

if __name__ == "__main__":
    main()
