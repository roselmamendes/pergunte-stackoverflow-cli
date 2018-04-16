import unittest
from pergunte_stackoverflow.terminal import Terminal
from pergunte_stackoverflow.questions import Questions
from pergunte_stackoverflow.answer import Answer


class TestTerminal(unittest.TestCase):
    def test_should_return_information_about_the_search(self):
        search_results = [Questions(1234, "How to handle dependencies in go", "algum.link", Answer())]
        for_output = {
            "endpoint": "stackoverflow.com/search/advanced?...",
            "search_results": search_results,
            "parameters": {
                "q": "",
                "sort": "relevance",
                "order": "desc",
                "site": "stackoverflow"
            }
        }
        output = Terminal.mount_output(for_output)

        self.assertIn("Endpoint: stackoverflow.com/search/advanced?...\nParameters: q= ; sort=relevance ; site=stackoverflow ; order=desc", output)

    def test_should_mount_the_output_with_the_search_results(self):
        best_answer = Answer()
        best_answer.title = "How to handle dependencies in go"
        best_answer.body = "some answer"
        best_answer.link = "some answer link"

        question1 = Questions(1234, "How to handle dependencies in go", "algum.link", best_answer)

        question2 = Questions(1234, "How to handle dependencies in go", "algum.link", best_answer)
        
        search_results = [question1, question2]
        
        for_output = {
            "endpoint": "stackoverflow.com/search/advanced?...",
            "search_results": search_results,
            "parameters": {
                "q": "",
                "sort": "relevance",
                "order": "desc",
                "site": "stackoverflow"
            }
        }
        output = Terminal.mount_output(for_output)

        self.assertIn("=========================================================\nHow to handle dependencies in go\n\nAnswer with higher score:\nSource: some answer link\nsome answer\n=========================================================\nHow to handle dependencies in go\n\nAnswer with higher score:\nSource: some answer link\nsome answer\n", output)
