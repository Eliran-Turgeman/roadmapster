from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")


class GPTUtility:
    client = OpenAI(
        api_key=config['OPENAI_API_KEY']
    )

    @staticmethod
    def prompt(msg: str, model: str = 'gpt-3.5-turbo'):
        """
        Prompts gpt model with msg
        :param msg: prompt
        :param model: type of openai model
        :return: model response
        """
        completion = GPTUtility.client.chat.completions.create(model=model, messages=[{"role": "user", "content": msg}])
        return completion.choices[0].text
