from data.current_quiz_data import fetch_current_quiz_data
from data.historical_quiz_data import fetch_historical_quiz_data
from analysis.data_analysis import analyze_performance
from analysis.insights_generation import generate_insights
from analysis.recommendations import create_recommendations
from analysis.persona import define_student_persona
from analysis.visualization import visualize_insights

def main():
    current_quiz_endpoint = 'CURRENT_QUIZ_API_ENDPOINT'
    historical_quiz_endpoint = 'HISTORICAL_QUIZ_API_ENDPOINT'
    
    current_quiz_data = fetch_current_quiz_data(current_quiz_endpoint)
    historical_quiz_data = fetch_historical_quiz_data(historical_quiz_endpoint)
    
    performance_data = analyze_performance(current_quiz_data, historical_quiz_data)
    insights = generate_insights(performance_data)
    recommendations = create_recommendations(insights)
    persona = define_student_persona(performance_data)
    
    print("Insights:", insights)
    print("Recommendations:", recommendations)
    print("Student Persona:", persona)
    
    visualize_insights(performance_data)

if __name__ == "__main__":
    main()