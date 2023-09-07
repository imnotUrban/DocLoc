import os
import json
import openai
# load env variables
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class GPTQueryEngine:
    def __init__(self):
        pass
    def __makePrompt(self,new: str) -> any:
        return f"""{new}
        Analyse the text above and return a JSON array as the result.
        the JSON data must be in Spanish.
        The JSON must have these fields: location, summary.
        Include only geographically valid and precise locations.
        Exclude temporal locations, non-terrestrial locations, non-spatial locations, individuals, companies, organizations, and fictional locations.
        The summary must be about the relevant event to the location.
        """
    def __getMessages(self,new: str) -> list:
        return [
            {"role": "system", "content": "You are a helpful tool for analyzing locations."},
            {"role": "user", "content": self.__makePrompt(new)},
        ]
    @staticmethod
    def __getFunction() -> list:
        return [
            {
        "name": "get_locations_and_summaries_from_text",
        "description": "From a text, extracts multiple locations and relevant summaries.",
        "parameters": {
        "type": "object",
        "properties": {
            "locations_and_summaries": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "the address in the format 'calle, ciudad, región, país'"
                        },
                        "summary": {
                            "type": "string",
                            "description": "The event relevant to location"
                        }
                    },
                    "required": ["location", "summary"],
                    "additionalProperties": False
                }
            }
        },
        "required": ["locations_and_summaries"]
    }
}
        ]

    def __analyze(self,new: str) -> str:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages= self.__getMessages(new),
            functions=self.__getFunction(),
        )
        try:
            generated_text = completion.choices[0].message.function_call.arguments
            return json.loads(generated_text)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    def query(self, new: str) -> any:
        return self.__analyze(new)
