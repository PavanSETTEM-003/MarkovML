import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification

# Load pre-trained BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = TFBertForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Load the trained weights
model.load_weights('D://markov ml//deployment//bert_sentiment_model_weights.h5')

def model_predictions(input_sentences):
    predicted_labels = []

    for input_sentence in input_sentences:
        # Preprocess and tokenize the input sentence
        input_sentence_encoded = tokenizer(input_sentence, padding=True, truncation=True, return_tensors="tf", is_split_into_words=True)

        # Make predictions
        predictions = model(input_sentence_encoded)
        logits = predictions.logits

        # Convert logits to probabilities
        probabilities = tf.nn.softmax(logits, axis=1)

        # Get the predicted class for the input sentence
        predicted_class = tf.argmax(probabilities, axis=1).numpy()[0]  # Assumes a single sentence input

        print(probabilities)
        print(predicted_class)

        # Define the class labels
        class_labels = [ 'Positive','Negative']

        # Get the corresponding label for the prediction
        predicted_label = class_labels[predicted_class]
        
        predicted_labels.append(predicted_label)

    return predicted_labels