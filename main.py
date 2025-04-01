import os
import openai
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

def main():
    # Set up OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    
    # If environment variable isn't set, you can hardcode it (not recommended for production)
    if not api_key:
        print("Please set the OPENAI_API_KEY environment variable")
        return
    
    try:
        client = openai.OpenAI(api_key=api_key)
        
        # Create a completion
        response = client.responses.create(
            model="gpt-4o",
            instructions="You are a coding assistant that talks like a pirate.",
            input="How do I check if a Python object is an instance of a class?",
        )

        print("Generated text:")
        print(response.output_text)
        
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
