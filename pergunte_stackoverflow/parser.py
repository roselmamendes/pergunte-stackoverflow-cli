from pergunte_stackoverflow.questions import Questions
from pergunte_stackoverflow.answer import Answer


def parse_questions_json_to_object(questions_json):
    questions_object = []
    for question_json in questions_json:
        questions_object.append(
            Questions(
                question_json["question_id"],
                question_json["title"],
                question_json["link"],
                None
            )
        )
        
    return questions_object

def parse_answer_json_to_object(answer_json):
    answer = Answer()

    answer.answer_id = answer_json["answer_id"]
    answer.title = answer_json["title"]
    answer.body = answer_json["body"]
    answer.link = answer_json["link"]
    answer.score = answer_json["score"]

    return answer
