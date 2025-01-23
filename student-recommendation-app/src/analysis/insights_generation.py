def generate_insights(performance_data):
    insights = {}
    
    # Example insight: Identify weak topics
    weak_topics = performance_data[performance_data['score'] < 50]['topic'].tolist()
    insights['weak_topics'] = weak_topics
    
    return insights

def highlight_performance_gaps(insights):
    gaps = {}
    for topic, data in insights['weak_areas'].items():
        gaps[topic] = {
            'average_score': data['average_score'],
            'improvement_needed': 50 - data['average_score']
        }
    return gaps

def generate_summary(insights):
    summary = {
        'weak_areas_count': len(insights['weak_areas']),
        'improvement_trends_count': len(insights['improvement_trends']),
        'performance_gaps': highlight_performance_gaps(insights)
    }
    return summary