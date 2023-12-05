import os
import json
import openai
from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")

openai.api_key = "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"
class GPTQueryEngine:
    def __init__(self):
        pass
    def __makePrompt(self,new: str) -> any:
        return f"""{new}"""
    def __getSystem(self):
        #TODO #2 pasar a archivo de config
        return '''
    Extract information from a location following the format 'Street, City, Region, Country' (e.g., Plaza de Mayo, Buenos Aires, Argentina; Paseo de la Reforma, Mexico City, Mexico).
    The extracted information should be in Spanish.
    Create a JSON with the following fields: location and summary.
    Absolutely do not include non-valid locations. Only include geographically valid and precise locations. Exclude temporal, non-terrestrial, non-spatial, individuals, companies, organizations, fictional locations. Exclude general terms like 'Hotel', 'Hospital', 'Carretera', 'Autopista' and exclude vague locations like 'tv shows' or 'radio station'.
    The summary should relate to the relevant event at the location and be brief. Remember, the location represents a real place or region.
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
            result = json.loads(generated_text)
            result["usage"] = completion.usage
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    def query(self, new: str) -> any:
        return self.__analyze(new)
