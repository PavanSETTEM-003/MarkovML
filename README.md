# Early Detection of Mental Health Conditions on Twitter: An NLP-Based Approach


## Abstract
The prevalence of mental health challenges in today’s digital age necessitates innovative methods for timely detection and support. This study leverages the power of natural language processing (NLP) and social media data, particularly Twitter, to identify early signs of mental health issues. By recognizing patterns indicative of mental health conditions like depression, anxiety, or stress, the project identifies at-risk individuals early in their struggles. The analysis of various models, including Naive Bayes, Support Vector Machine (SVM), LSTM, and BERT, underscores BERT’s superiority due to its consistent performance across precision, recall, F1-score, and accuracy metrics. BERT’s contextual language understanding and adaptability across different data sources, exemplified by its success with Reddit data, position it as a robust solution for this task. MarkovML has proven invaluable by seamlessly integrating bookkeeping, facilitating nuanced comparisons, and enhancing exploratory data analysis, significantly streamlining project workflows and bolstering informed decision-making processes.
```
.
├── Datasets
│   ├── Cleaned_Reddit.csv
│   ├── Cleaned_Tweets_stopwords.csv
│   ├── Data Sources
│   │   ├── Reddit.xlsx
│   │   ├── sentiment_tweets3.csv
│   │   ├── tweets_combined.csv
│   │   └── Twitter_Non-Advert.xlsx
│   ├── Pre-Processing_Data.ipynb
│   └── Tweets_data.ipynb
├── Docs
│   ├── EDA_Team_2.pdf
│   ├── Final_Report_Team2.pdf
│   ├── Project_Proposal.pdf
│   └── Project Scope_Team2.pdf
├── Models
│   ├── Bert-Classifier.ipynb
│   ├── LSTM.ipynb
│   ├── MarkovML Registered
│   │   ├── BERT-Registered.ipynb
│   │   ├── LSTM_Registered.ipynb
│   │   └── SVM-Registered.ipynb
│   ├── Naive_Bayes.ipynb
│   └── SVM.ipynb
├── README.md
├── requirements.txt
└── Web-Dev
    ├── static
    │   ├── media
    │   │   └── brain.png
    │   └── style.css
    ├── templates
    │   ├── index.html
    │   └── test_page.html
    ├── preprocess.py  
    ├── utils.py
    └── website.py
```

<p>It is recommended to run the project in a virtual environment (venv) to avoid library clashes. This isolates Python packages for different projects, ensuring different versions of the same package can be used without conflicts. Running the project in a venv also prevents any project-specific packages from polluting your system Python installation.</p>

<p>Make sure you have Python's <code>venv</code> package installed. If not, install it by running the following command:</p>

<pre><code>pip install virtualenv</code></pre>

<h2>Setup and Run Instructions</h2>

<p>To set up and run the project locally, follow the steps below:</p>

<ol>
  <li>Open a new folder, create a virtual environment, and activate it:</li>

  <pre><code>python -m venv markovml_virtualenv</code></pre>

  <p>On Windows:</p>

  <pre><code>.\markovml_virtualenv\Scripts\activate</code></pre>

  <p>On Unix/Linux:</p>

  <pre><code>source markovml_virtualenv/bin/activate</code></pre>

  <li>Clone this repository and navigate to the cloned repository:</li>

  <pre><code>git clone https://github.com/PavanSETTEM-003/MarkovML.git</code></pre>

  <pre><code>cd MarkovML </code></pre>

  <li>Install the required dependencies:</li>

  <pre><code>pip install -r requirements.txt</code></pre>

  <li>Dowload Model weights</li>
  <p>

The model weights used in this project : [Google Drive Model Weights](https://drive.google.com/drive/folders/16K36oWUfh_upLUGABsC2mrO1vMdASXnu)

Modify the line no 10 in the `utils.py` file to match the location of the downloaded model weights on your local machine.

   ```python
   # In utils.py
   model.load_weights("path to the downloaded weights in your local machine")
   ```
  </p>

<h2>Run the Flask File</h2>
<p>
    Navigate to the 'Web-Dev' folder where the Flask application, 'website.py', is located.
    Run the Flask application by executing the following command:

   ```python
   python website.py
   ```
![Home_page](https://github.com/PavanSETTEM-003/MarkovML/assets/88257205/582951c6-0f00-4e1d-8dd3-639e9df4775b)
![Test_page](https://github.com/PavanSETTEM-003/MarkovML/assets/88257205/a6ee3419-51cf-43fa-8431-c53b27587f2b)


</p>


<h2></h2>
🙌 We highly value your feedback as it enables us to continuously improve the functionality and usability of the code. 🚀
