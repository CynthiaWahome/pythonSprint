import unittest 

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What Language?"

        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")

        self.assertIn('English', my_survey.responses)
        #self.assertEqual('What Language?', my_survey.show_question())

    def test_show_question(self):
        question = "what language?"

        my_survey = AnonymousSurvey(question)
        self.assertEqual("what language?", my_survey.show_question())


    def test_store_three_responses(self):
        question = "What lang?"
        my_survey = AnonymousSurvey(question)

        responses = ["English", "Kisii", "Mandarin"]

        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()
