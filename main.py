import os
from dotenv import load_dotenv
from google import genai

def main():
    # Load in env variables
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("API Key Invalid (is it missing?)")
    
    client = genai.Client(api_key=api_key)

    # Hard coding the prompt
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )

    # Keep track of token usage
    usage = response.usage_metadata

    if usage.prompt_token_count is None:
        raise RuntimeError("API Request failed. Please try again.")

    # Check how many tokens we're using
    print("Prompt tokens:", usage.prompt_token_count, "\nResponse tokens:", usage.candidates_token_count)

    # Print the models response to the cli
    print(response.text)

if __name__ == "__main__":
    main()
