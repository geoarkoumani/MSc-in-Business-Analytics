
# MSc in Business Analytics - AUEB
# Machine Learning and Content Analytics – Mini Project

# Offensive language and hate speech detection

The aim of the particular AUEB project was to implement a machine learning idea that provides a solution to a specific problem.
Thus, offensive language and hate speech detection case was chosen using datasets that contained comments from various platforms across the internet (e.g. YouTube, Reddit, TikTok, Twitter, [hatebase](https://hatebase.org/) etc).

The project consists of: 
- a complete business idea
- dataset selection 
- data preparation & exploratory analysis
- text analysis
- sentiment analysis
- model training & evaluation
- error analysis
- a UI application implementation using Streamlit
- application deployment with Streamlit Cloud






# Table of Contents
- [Business Case](#business-case)
- [Requirements](#requirements)
- [Code](#code)
    - [Run code](#run-code)
- [Datasets](#datasets)
    - [Final dataset](#final-dataset)
- [Models](#models)
- [Streamlit application](#streamlit-application)
    - [Installation](#installation)
    - [Run the application](#run-the-application)
    - [Streamlit Cloud](#streamlit-cloud)
    - [hateless app](#hateless-app)
- [Future Work](#future-work)

# Business Case
Our start-up company QC Greece was first established in 2021 from a group of friends, who wanted with their product to contribute to the elimination of offensive language in social media. QC Greece is an Information Technology and data-driven company that provides the ‘hateless’ app, an application created with machine learning and neural network algorithms.

Our team is specialized in data analysis and representation with User Interfaces of the actual results in order to determine the corresponding solutions.

Our mission is to detect and eliminate offensive language from social media and various platforms through the internet. Also, we provide our services to our clients (smaller or bigger companies) in order to find effective solutions in social media platforms, such as banning users whose comments are rather offensive to other community members.

# Requirements
In addition to the built-in Python, Anaconda & Streamlit distribution libraries, external libraries and packages were also installed.

Prerequisite for the project was the creation and addition to the GitHub repository of a file: **requirements.txt** containing all the required packages and libraries. 

A list of the aforementioned installed libraries via [PyPi](https://pypi.org/) is:
- [pyspellchecker](https://pypi.org/project/pyspellchecker/)
- [autocorrect](https://pypi.org/project/autocorrect/)
- [nltk](https://www.nltk.org/install.html)
- [textblob](https://pypi.org/project/textblob/)
- [scikit-learn](https://pypi.org/project/scikit-learn/)
- [keras](https://pypi.org/project/keras/)
- [tensorflow](https://www.tensorflow.org/install)
- [spacy](https://pypi.org/project/spacy/)
- [textstat](https://pypi.org/project/textstat/)
- [wordcloud](https://pypi.org/project/wordcloud/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [seaborn](https://seaborn.pydata.org/installing.html)
- [imblearn](https://pypi.org/project/imbalanced-learn/)
- [pprint](https://pypi.org/project/pprintpp/)
- [nlpaug](https://pypi.org/project/nlpaug/)
- [pycopy-collections.defaultdict](https://pypi.org/project/pycopy-collections.defaultdict/)

Also, in order to load the required datasets from [Hugging Face](https://huggingface.co/datasets) the following installation was performed:
```bash
pip install datasets
```

# Code
The implementation of the code is created in execution ordering. 
- `1 Data preparation.ipynb`
- `2.1 EDA Text Analysis.ipynb`
- `2.2 EDA Text Analysis - Berkeley Analysis`
- `3. CNN RNN Models`
- `4.1. Text Analysis for ML Models`
- `4.2. BERT Model`
- `4.3. Sentiment Analysis with VADER`
# Run code
Using [Jupyter Notebook](https://jupyter.org/install) or [Google Colaboratory](https://colab.research.google.com/?utm_source=scs-index) by executing the code blocks.
# Datasets
As per data preparation, 6 different datasets were used from official sources in order to obtain real-world data and train the models effectively. 
In particular, the datasets used are: [Berkeley Dataset](https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech) (consists of 39,565 comments annotated by 7,912 annotators, for 135,556 combined rows and 131 columns. The primary outcome variable is the "hate speech score" but the 10 constituent labels (sentiment, (dis)respect, insult, humiliation, inferior status, violence, dehumanization, genocide, attack/defense, hate speech benchmark) can also be treated as outcomes. Includes 8 target identity groups (race/ethnicity, religion, national origin/citizenship, gender, sexual orientation, age, disability, political ideology) and 42 identity subgroups), [ethos Dataset](https://huggingface.co/datasets/ethos) (consists of 998 comments (rows) and 2 columns in the dataset alongside with a label about hate speech presence or absence. 565 of them do not contain hate speech, while the rest of them, 433, contain), [ICWSM18 Dataset](https://www.icwsm.org/2018/datasets/datasets/) (consists of 3222 comments (rows) and 10 columns: id, title, type, message, class  & sub 1 to 5 while it contains approximately 75% of hate speech), [All-in-One Jigsaw Dataset](https://www.kaggle.com/code/adldotori/all-in-one-dataset/data) (consists of 2223065 rows and 11 columns with an id, a comment, the main target, the other toxicity subtypes as well as identity attributes), [Davidson Dataset](https://huggingface.co/datasets/hate_speech_offensive) (consists of 24783 rows and 6 columns with hate and offensive speech counts and classes along with the corresponding comment/tweet) & [CONAN Dataset](https://github.com/marcoguerini/CONAN) (consists of 5003 rows and 5 columns with counter narrative pairs covering the multiple hate targets, including DISABLED, JEWS, MIGRANTS etc. Each pair is provided along with its loop information (VERSION), and its target (TARGET). The dataset contains only hate speech.).

All the datasets used are stored in Google Drive and can be accessed [here](https://drive.google.com/drive/folders/1nqMWvCb6EhsqY4Q1C0XGu5m2m_qsvD3K).
## Final dataset
After an extended data preparation & cleaning and text & EDA analysis, the final dataset that is used to train the models consists of: **1381262** *rows/comments* and **2** columns: *category* & *lemmatized*.
# Models
The models that were trained in order to find the best that decides whether a comment is offensive or not are:
- [BoW / TF-IDF Vectorizers](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [Linear SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html)
- [K Neighbors Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
- [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [Naive Bayes Multinomial Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)
- [ΒΕRT](https://www.tensorflow.org/text/tutorials/classify_text_with_bert#about_bert)
- [Recurrent Neural Networks Model (RNN)](https://www.tensorflow.org/guide/keras/rnn)
- [Convolutional Neural Networks Model (CNN)](https://www.tensorflow.org/tutorials/images/cnn)

Also, a sentiment analysis was also implemented using [VADER](https://pypi.org/project/vaderSentiment/).

The weights of the respective models are stored in Google Drive and can be accessed [here]().
# Streamlit application
[Streamlit](https://streamlit.io/) is an open-source app framework for Machine Learning and Data Science teams that lets you turn data scripts into shareable web apps using Python.

![Example of live coding an app in Streamlit|635x380](https://github.com/streamlit/docs/raw/main/public/images/Streamlit_overview.gif)

For the needs of identifying hate and offensive language, Streamlit was a prerequisite in order to build a User Interface that helps the user analyze any preferable comments.
## Installation
The prerequisites for the Streamlit working environment setup was to create a conda environment, after the installation of Anaconda. For the needs of this application Python 3.9.12 version was used.

```bash
conda create -n streamlit python=3.9.12 anaconda
conda activate streamlit
pip install streamlit
```
## Run the application
```bash
streamlit run app.py
```

The application runs successfully on http://localhost:8501/.
## Streamlit cloud
The application has been deployed in the Streamlit Cloud. You can access here: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://machine-learning-and-content-analyticsoffensive-langua-eld23e.streamlitapp.com/)
## hateless app
***hateless*** is a sentiment analysis application designed for analyzing comments from various platforms through the internet and identifying if they are offensive or not. The user logs in the application and then writes the corresponding comment that he/she wants to analyze in the respective placeholder and by pressing the ‘Analyze’ button, starts the analysis.

The output of the analysis consists of 3 different sections: ***Sentiment metrics***, ***Sentiment token metrics*** & ***Sentiment metrics visualization***. 

In the *first* section, two basic sentiment metrics are represented: **polarity** (lies between [-1,1], -1 defines a negative sentiment and 1 defines a positive sentiment, negative words reverse the polarity) & **subjectivity** (quantifies the amount of personal opinion and factual information contained in the text, the higher subjectivity means that the text contains personal opinion rather than factual information) along with the overall sentiment that the comment provokes to a user with labels: **Positive**, **Negative**  or **Neutral**. 

In the *second* section, using **SentimentIntensityAnalyzer** from VADER, 3 lists (**positives**, **negatives** & **neutrals**) with sentence tokens are represented, based on their polarity scores. A *threshold* of 0.1 has been chosen in order to categorize the tokens of the sentence. If the score is > 0.1, then the token will be moved to the positive list, if the score is <= -0.1, then it will be moved to the negative list and otherwise to the neutral list. 

In the *third* section, a bar chart is represented with the 2 basic metrics mentioned above: **polarity** & **subjectivity**. Also, a variety of actions are available in this section e.g. zoom-in, zoom-out, download the graph etc.
# Future Work
After the corresponding research and training of different models, we identify and examine challenges faced by various approaches for hate speech detection in texts. Among these difficulties are misspellings, human errors while writing a text/comment, autocorrections and in general imbalanced data that can make detecting hate speech a challenging task. The computational cost of the algorithms used to train the models should also be mentioned as a difficulty.
Also, it is noticeable that accuracy has been one of the main offensive language recognition challenges for many years – and a barrier to entry for many businesses. 

The main aim is to expand the applications' features to support more funcionalities e.g. setting up a Registration page, User App Dashboard, Addon for connecting social media accounts etc. More information is demonstrated in our report.

As per implementation, the application is on a bug fixing mode regarding the deployment phase and some corrective actions will be performed in the future before the production stage. 