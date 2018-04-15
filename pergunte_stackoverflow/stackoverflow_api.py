import requests
from pergunte_stackoverflow.parser import parse_questions_json_to_object, parse_answer_json_to_object

ANSWER_FILTER = "!4*fdm68f3jJlYcwPP"

class StackoverflowApi:
    def search(keyword):
        response = requests.get(_questions_url(keyword))

        questions_json = response.json()["items"]

        questions_json = StackoverflowApi._remove_unanswered_questions(questions_json)
        
        questions_object = parse_questions_json_to_object(questions_json)

        StackoverflowApi._mount_the_questions_with_the_best_answer(questions_object)

        return questions_object

    @staticmethod
    def _remove_unanswered_questions(questions_json):
        return filter(lambda q: q["is_answered"], questions_json)
    
    @staticmethod
    def _mount_the_questions_with_the_best_answer(questions_object):
        for question_object in questions_object:
            StackoverflowApi._get_best_answer_for(question_object)
    
    @staticmethod
    def _get_best_answer_for(question_object):
        response = requests.get(_answer_url(question_object.question_id))

        best_answer_json = StackoverflowApi._find_the_best_score(response.json()["items"])
        question_object.best_answer = parse_answer_json_to_object(best_answer_json)

    @staticmethod
    def _find_the_best_score(answers):
        return max(answers, key=_get_score_of)
        
def _questions_url(keyword):
    return 'https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=relevance&q={}&site=stackoverflow'.format(keyword)

def _answer_url(question_id):
    return "https://api.stackexchange.com/2.2/questions/{}/answers?order=desc&sort=activity&site=stackoverflow&filter={}".format(question_id, ANSWER_FILTER)

def _get_score_of(answer):
    return answer["score"]
