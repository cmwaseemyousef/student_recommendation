# Personalized Student Recommendations

## Project Overview
This project analyzes quiz performance data to provide students with personalized recommendations to improve their preparation.

## Setup Instructions
1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the main script:
    ```bash
    python src/main.py
    ```

## Approach Description
1. Fetch current and historical quiz data from provided endpoints.
2. Analyze quiz performance by topics, difficulty levels, and response accuracy.
3. Generate insights to highlight weak areas, improvement trends, and performance gaps.
4. Create recommendations for actionable steps to improve.
5. Define student persona based on performance patterns.
6. Visualize key insights.

## Key Features
- Personalized analysis of quiz performance.
- Identification of weak areas and improvement trends.
- Actionable recommendations for enhancing quiz preparation.

## Future Enhancements
- Integration of machine learning algorithms for predictive analytics.
- User interface for better interaction and visualization of insights.

## License
This project is licensed under the MIT License.
