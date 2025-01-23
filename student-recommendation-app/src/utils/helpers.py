def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

def format_quiz_data(quiz_data):
    formatted_data = []
    for question in quiz_data:
        formatted_data.append({
            'question_id': question['id'],
            'selected_option': question['selected_option'],
            'correct_option': question['correct_option'],
            'topic': question['topic'],
            'difficulty': question['difficulty']
        })
    return formatted_data

def identify_weak_areas(performance_data):
    weak_areas = {}
    for topic, scores in performance_data.items():
        average_score = calculate_average(scores)
        if average_score < 50:  # Assuming 50 is the threshold for weak performance
            weak_areas[topic] = average_score
    return weak_areas

def calculate_improvement_trend(scores):
    if len(scores) < 2:
        return None
    return scores[-1] - scores[0]

def label_student_performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Needs Improvement"