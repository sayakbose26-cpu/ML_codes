from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.pipeline import Pipeline
data={
    "text": ["I love this movie", "This movie is terrible", "Great film, highly recommended"],
    "sentiment": ["positive", "negative", "positive"]
}
df = pd.DataFrame(data)
x = df["text"]
y = df["sentiment"]
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])
model.fit(x, y)
text = input("Enter a text to predict sentiment: ")
prediction = model.predict([text])
print(prediction[0])