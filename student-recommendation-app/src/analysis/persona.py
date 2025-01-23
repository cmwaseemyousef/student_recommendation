def define_student_persona(performance_data):
    persona = {}
    
    # Example persona: Identify strengths and weaknesses
    strengths = performance_data[performance_data['score'] >= 80]['topic'].tolist()
    weaknesses = performance_data[performance_data['score'] < 50]['topic'].tolist()
    
    persona['strengths'] = strengths
    persona['weaknesses'] = weaknesses
    
    return persona