import unittest
import requests_mock
from pergunte_stackoverflow.stackoverflow_api import StackoverflowApi


class TestStackoverflowApi(unittest.TestCase):
    @requests_mock.mock()
    def test_should_get_questions_about_docker(self, m):
        m.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&tagged=docker&site=stackoverflow',
              json={
                  "items":[
                      {"question_id": 1234, "title": "O que é docker", "link": "https://algum.link"}
                  ]
              })

        m.get("https://api.stackexchange.com/2.2/questions/1234/answers?order=desc&sort=activity&site=stackoverflow",
              json={"items":[
                  {
                      "score": 3,
                      "answer_id": 5678,
                      "title": "An example post title",
                      "body": "An example post body",
                      "link": "algum.link"
                  }
              ]})
        
        found_questions = StackoverflowApi.search('docker')

        self.assertEqual("O que é docker", found_questions[0].title)
        self.assertEqual("https://algum.link", found_questions[0].link)
        self.assertIsNotNone(found_questions[0].best_answer)

    @requests_mock.mock()
    def test_should_the_question_come_with_the_best_response(self, m):
        m.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&tagged=docker&site=stackoverflow',
              json={
                  "items":[
                      {"question_id": 1234, "title": "O que é docker", "link": "https://algum.link"}
                  ]}
        )
        m.get("https://api.stackexchange.com/2.2/questions/1234/answers?order=desc&sort=activity&site=stackoverflow",
              json={"items":[
                  {
                      "score": 3,
                      "answer_id": 5678,
                      "link": "http://example.stackexchange.com/questions/1234/an-example-post-title/5678#5678",
                      "title": "An example post title",
                      "body": "An example post body"
                  },
                  {
                      "score": 1,
                      "answer_id": 1234,
                      "link": "algum.link",
                      "title": "some title",
                      "body": "some body"
                  }
              ]})
        
        found_questions = StackoverflowApi.search('docker')
        
        self.assertEqual("An example post body", found_questions[0].best_answer.body)
