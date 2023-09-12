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
        return f"""{new}"""
    def __getSystem(self):
        #TODO #2 pasar a archivo de config
        return '''
A location is a term that is spatial, geographic, real-world, either natural or man-made, addressable, cartographic, navigable, observable, and existing in the tangible physical realm.
Specify what a location is NOT by excluding the terms temporal, non-terrestrial, non-spatial, individuals, companies, organizations, and fictional locations.
Task: Extract information and analyze the text to create a JSON while ensuring that non-valid locations are not included under any circumstance.
Instructions:
1. Extract information from locations following the format 'Street, City, Region, Country' (e.g., Barrio San Martín, Buenos Aires, Argentina; Carrera 7 #789, Bogotá, Colombia). Locations should be filled in from left to right.
2. The extracted information should be in Spanish.
3. Create a JSON with the following fields: location and summary.
4. Absolutely do not include non-valid locations. Only include geographically valid and precise locations. Exclude temporal, non-terrestrial, non-spatial, individuals, companies, organizations, fictional locations. Exclude general terms like 'Hotel', 'Hospital', 'Carretera', 'Autopista' and exclude vague locations like 'tv shows' or 'radio station'
5. The summary should relate to the relevant event at the location and be brief.
Remember locations represent real places or regions.
'''
    def __getMessages(self,new: str) -> list:
        return [
            {"role": "system", "content": self.__getSystem()},
            {"role": "user", "content": self.__makePrompt(new)}
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
            "data": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "the address in address format: 'street, city, region, country'"
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
        "required": ["data"]
    }
}
        ]

    def __analyze(self,new: str) -> str:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages= self.__getMessages(new),
            functions=self.__getFunction(),
            temperature=0.1
        )
        try:
            generated_text = completion.choices[0].message.function_call.arguments
            print(completion.usage.prompt_tokens,completion.usage.completion_tokens,completion.usage.total_tokens)
            return json.loads(generated_text)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    def query(self, new: str) -> any:
        return self.__analyze(new)
