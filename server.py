"""
server.py

This module is used to run the Flask server
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def home():
    """
    Renders the homepage
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emo_detector():
    """
    Takes in user text input and feeds it to the machine learning model
    to generate an emotions report and displays it to the user
    """
    # Get user text input
    text = request.args.get("textToAnalyze")

    response = emotion_detector(text)

    dominant = response.pop("dominant_emotion")

    # If dominant_emotion is None, then the input text was invalid
    if dominant is None:
        return "Invalid input! Try again.", 500

    # Return formatted response
    return f"""For the given statement, the system response is
    {', '.join([f"'{key}': {str(val)}" for key, val in response.items()])}.
    The dominant emotion is <b>{dominant}</b>.""", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
