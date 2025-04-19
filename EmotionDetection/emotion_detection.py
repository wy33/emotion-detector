import requests, json

def emotion_detector(text_to_analyse):
    # Emotion Predict function from the Watson NLP library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }
    
    # Access API to get prediction and format to dictionary
    response = requests.post(url, json=data, headers=headers)
    formatted_response = json.loads(response.text)

    dominant_emotion = None
    emotion_predictions = {}
    if response.status_code == 200:
        # Extract emotions and scores
        emotion_predictions = formatted_response["emotionPredictions"][0]["emotion"]

        # Find dominant emotion
        dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)

    # Add dominant emotion to dictionary
    emotion_predictions.update({"dominant_emotion": dominant_emotion})

    # Final Format:
    # {
    # 'anger': anger_score,
    # 'disgust': disgust_score,
    # 'fear': fear_score,
    # 'joy': joy_score,
    # 'sadness': sadness_score,
    # 'dominant_emotion': '<name of the dominant emotion>'
    # }
    # NOTE: if the response is an error, then only "dominant_emotion" 
    #   with a value of None will be in the dictionary
    return emotion_predictions
