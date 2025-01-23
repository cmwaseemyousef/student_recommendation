from typing import Dict, Any
import requests

class CurrentQuizData:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.quiz_data = self.fetch_quiz_data()

    def fetch_quiz_data(self) -> Dict[str, Any]:
        # Replace with the actual API endpoint for fetching current quiz data
        api_endpoint = f"https://api.example.com/quiz/current/{self.user_id}"
        return fetch_current_quiz_data(api_endpoint)

    def process_quiz_data(self) -> Dict[str, Any]:
        # Process the fetched quiz data as needed
        processed_data = {
            "questions": self.quiz_data.get("questions", []),
            "topics": self.quiz_data.get("topics", []),
            "responses": self.quiz_data.get("responses", {}),
            "score": self.quiz_data.get("score", 0),
        }
        return processed_data

    def get_quiz_summary(self) -> Dict[str, Any]:
        # Generate a summary of the quiz performance
        processed_data = self.process_quiz_data()
        summary = {
            "total_questions": len(processed_data["questions"]),
            "score": processed_data["score"],
            "topics_covered": processed_data["topics"],
        }
        return summary

def fetch_current_quiz_data(api_endpoint):
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()