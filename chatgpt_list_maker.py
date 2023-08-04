from dotenv import load_dotenv
import os
load_dotenv(".gitignore/secrets.sh")
import openai

from dotenv import load_dotenv
import os
import openai

load_dotenv(".gitignore/secrets.sh")

def chatgpt(prompt):
    # define OpenAI key
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    # Generate a list
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )

    # Get the text from the response
    text = response.choices[0].text.strip()

    # Split the text into a list of plant descriptions
    # This example assumes each plant description is on a new line
    descriptions = text.split('\n')

    # Filter the list to only include plants that are in your database
    # And split each description into the first word (common name) and the rest
    plants = [(desc.split(' ', 1)[0], desc) for desc in descriptions if desc.split(' ', 1)[0] in database_plants]

    # Now plants is a list of tuples, where each tuple contains the common name and the full description

    # To get a list of the common names only, you can do:
    common_names = [plant[0] for plant in plants]

    # To get a list of the full descriptions only, you can do:
    full_descriptions = [plant[1] for plant in plants]

    # To store the entire response as a string, you can do:
    response_string = '\n'.join(full_descriptions)

    print(common_names)
    print(response_string)
