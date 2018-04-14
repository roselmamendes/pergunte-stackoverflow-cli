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
    return Answer(
        answer_json["answer_id"],
        answer_json["title"],
        answer_json["body"],
        answer_json["link"],
        answer_json["score"]
    )
