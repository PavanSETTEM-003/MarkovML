#%%
import markov
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras.layers import Dense

# ! markov init --api-token=7SQQr7x6X2PWY9YdcqMdzwFS  

#%%

def run_experiments(parameters):

    try:
        # Read the data from the CSV file into a Pandas DataFrame
        data = pd.read_csv('D:\markov ml\gui\Cleaned_Tweets_stopwords.csv')

        tweets = data['cleaned_text']
        labels = data['label']

        # Create a CountVectorizer object for converting text data into a matrix of token counts
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(tweets)

        # Convert the sparse matrix to a dense numpy array
        X = X.toarray()

        # Split the data into training and testing sets (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

        # Convert labels to one-hot encoding
        num_classes = len(np.unique(labels))
        y_train_onehot = pd.get_dummies(y_train).values
        y_test_onehot = pd.get_dummies(y_test).values

        # Create a Multinomial Naive Bayes model in Keras
        model = Sequential()
        model.add(Dense(num_classes, input_shape=(X_train.shape[1],), activation='softmax'))

        ## declared the hyper tuning parameters
        loss = 'categorical_crossentropy'
        optimizer = 'adam'
        epochs = 2
        batch_size = 10

        # model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
        # model.fit(X_train, y_train_onehot, epochs=epochs, batch_size=batch_size, validation_split=0.1)

        markov.keras.auto_record(
            name= parameters['model_name'],
            notes="testing",
            project_id="kFKnHV6AFD9CSg" # Demo Project Team - 2
        )

        #{'model_name': 'testing #3', 'Epochs': '1', 'Batch_size': '32', 'optimizer_name': 'adam', 'Loss': 'Categorical cross-entropy'}

        loss = parameters["Loss"] if(parameters["Loss"]) else loss
        optimizer = parameters["optimizer_name"] if(parameters["optimizer_name"]) else optimizer
        epochs = int(parameters["Epochs"]) if(parameters["Epochs"]) else epochs
        batch_size = int(parameters["Batch_size"]) if(parameters["Batch_size"]) else batch_size

        model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
        model.fit(X_train, y_train_onehot, epochs=epochs, batch_size=batch_size, validation_split=0.1)

        return True, "---model triggered---"

    except  Exception as error:
        return False, str(error)


if __name__ == "__main__":

    print("------done------")
