import unittest
import requests_mock
from pergunte_stackoverflow.stackoverflow_api import StackoverflowApi


class TestStackoverflowApi(unittest.TestCase):
    @requests_mock.mock()
    def test_should_get_questions_about_docker(self, m):
        m.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&tagged=docker&site=stackoverflow', json=
              {"items":
               [
                   {"title": "O que é docker", "link": "https://algum.link"}
               ]
              })
        
        found_questions = StackoverflowApi.search('docker')

        self.assertEqual("O que é docker", found_questions[0].title)
        self.assertEqual("https://algum.link", found_questions[0].link)

    @requests_mock.mock()
    def test_should_the_question_come_with_the_best_response(self, m):
        # self.assertEqual("O que é docker", found_questions[0].best_answer)
        pass
