from typing import List, Dict, Any
import requests

def fetch_historical_quiz_data(api_endpoint):
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

class HistoricalQuizData:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.historical_data = self.fetch_historical_data()

    def fetch_historical_data(self) -> List[Dict[str, Any]]:
        # Replace with the actual API endpoint
        api_endpoint = f"https://api.example.com/historical_quiz_data/{self.user_id}"
        return fetch_historical_quiz_data(api_endpoint)

    def get_performance_summary(self) -> Dict[str, Any]:
        summary = {
            "total_quizzes": len(self.historical_data),
            "average_score": self.calculate_average_score(),
            "topic_performance": self.analyze_topic_performance(),
        }
        return summary

    def calculate_average_score(self) -> float:
        total_score = sum(quiz['score'] for quiz in self.historical_data)
        return total_score / len(self.historical_data) if self.historical_data else 0.0

    def analyze_topic_performance(self) -> Dict[str, float]:
        topic_scores = {}
        for quiz in self.historical_data:
            for topic, score in quiz['topic_scores'].items():
                if topic not in topic_scores:
                    topic_scores[topic] = []
                topic_scores[topic].append(score)

        average_topic_scores = {topic: sum(scores) / len(scores) for topic, scores in topic_scores.items()}
        return average_topic_scores