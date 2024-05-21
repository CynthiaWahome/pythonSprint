import unittest 

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'kisii', 'pokomo']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])

        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_show_question(self):
        self.assertEqual("What language?", self.my_survey.show_question())


    def test_store_three_responses(self):

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
