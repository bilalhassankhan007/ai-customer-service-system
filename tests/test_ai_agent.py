import unittest
from ai_agent import AIAgent

class TestAIAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AIAgent()

    def test_respond_to_query(self):
        self.assertEqual(self.agent.respond_to_query("What are your hours?"), "We are open from 9 AM to 5 PM, Monday to Friday.")
        self.assertIsNone(self.agent.respond_to_query("Unknown query"))

if __name__ == '__main__':
    unittest.main()
