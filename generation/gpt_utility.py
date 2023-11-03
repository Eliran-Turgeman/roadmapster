import openai


class GPTUtility:
    @staticmethod
    def prompt(self, msg: str, model: str = 'gpt-3.5-turbo'):
        completion = openai.ChatCompletion.create(model=model, message=[{"role": "user", "content": msg}])
        return completion.choices[0].text
