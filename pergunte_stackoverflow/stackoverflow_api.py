import requests
from pergunte_stackoverflow.questions import Questions


class StackoverflowApi:
    def search(keyword):
        response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&tagged={}&site=stackoverflow'.format(keyword))

        questions = response.json()["items"]

        questions_object = StackoverflowApi._parse_json_to_object(questions)

        return questions_object

    @staticmethod
    def _parse_json_to_object(questions_json):
        questions_object = []
        for question_json in questions_json:
            questions_object.append(
                Questions(
                    question_json["title"],
                    question_json["link"]
                )
            )
        return questions_object
