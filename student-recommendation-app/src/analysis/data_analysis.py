import pandas as pd

def analyze_performance(current_quiz_data, historical_quiz_data):
    # Convert data to DataFrame for analysis
    current_df = pd.DataFrame(current_quiz_data)
    historical_df = pd.DataFrame(historical_quiz_data)
    
    # Example analysis: Calculate average score by topic
    topic_performance = historical_df.groupby('topic')['score'].mean().reset_index()
    
    return topic_performance


def identify_response_accuracy(current_quiz_data, historical_quiz_data):
    # Identify response accuracy for the current quiz
    accuracy_analysis = {}
    
    for question_id, selected_option in current_quiz_data['responses'].items():
        correct_option = current_quiz_data['correct_answers'][question_id]
        accuracy_analysis[question_id] = {
            'selected_option': selected_option,
            'correct_option': correct_option,
            'is_correct': selected_option == correct_option
        }
    
    return accuracy_analysis


def generate_performance_report(performance_analysis, accuracy_analysis):
    # Generate a report summarizing performance analysis and accuracy
    report = {
        'performance_analysis': performance_analysis,
        'accuracy_analysis': accuracy_analysis
    }
    
    return report