import matplotlib.pyplot as plt

def visualize_insights(performance_data):
    performance_data.plot(kind='bar', x='topic', y='score')
    plt.title('Performance by Topic')
    plt.xlabel('Topic')
    plt.ylabel('Average Score')
    plt.show()