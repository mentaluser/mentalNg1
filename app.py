import collections.abc
#hyper needs the four following aliases to be done manually.
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping

#Import libraries
from collections import Counter

# Flask
from flask import Flask, request, render_template
from openai import OpenAI

# handle warnings
import warnings
warnings.filterwarnings("ignore")

#Save and load the model
import joblib


# Set openai api key
api_key = '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'

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


# declare the app
app = Flask(__name__)

# variables
option_dict = {
    0 : 'Not at all',
    1 : 'Just a little',
    2 : 'Often',
    3 : 'Very Often'
}

prediction_data = {}

class MIS_Modeller():
    def __init__(self):
        self.model1 = joblib.load('models/model_xgboost.pkl')
        self.model2 = joblib.load('models/model_lgbm.pkl')
        self.model3 = joblib.load('models/model_logistic.pkl')
        self.scaler = joblib.load('models/scaler.pkl')
        self.label_encoder = joblib.load('models/label_encoder.pkl')
        self.mapping = dict(zip(range(len(self.label_encoder.classes_)), self.label_encoder.classes_))


    def prediction(self, data):
        data = self.scaler.transform(data)
        
        # model predictions
        pred1 = self.model1.predict(data)
        pred2 = self.model2.predict(data)
        pred3 = self.model3.predict(data)
        
        pred = []
        pred_prob = []
        # probability
        pred_prob1 = self.model1.predict_proba(data)
        pred_prob2 = self.model2.predict_proba(data)
        
        if list(pred1):
            pred.append(pred1[0])
        if list(pred2):
            pred.append(pred2[0])
        if list(pred3):
            pred.append(pred3[0])
        if list(pred_prob1):
            pred_prob.append(pred_prob1[0].max())
        if list(pred_prob2):
            pred_prob.append(pred_prob2[0].max())
        if pred and pred_prob:
            result = self.voting_aggregator(pred, pred_prob)
            return result
        return None
        
    def voting_aggregator(self, scores, pred_prob):
        result = Counter(scores)
        result = result.most_common(1)[0][0]
        result = self.mapping.get(result)
        prob = round((sum(pred_prob)/len(pred_prob))*100, 1)
        prediction = {"prediction":result, "confidence level":prob}
        return prediction

predictor = MIS_Modeller()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/diagnosis', methods=['GET'])
def diagnosis():    
    return render_template('adhd_form.html')

@app.route('/performance', methods=['GET', 'POST'])
def performance():
    if request.method == 'POST':
        try:
            data = process_form(request.form)
            result = predictor.prediction([data])
            prediction_data['prediction'] = result['prediction']
            prediction_data['confidence level'] = result['confidence level']
        except Exception as e:
            print(e)
            return render_template('adhd_form.html')
        else:
            return render_template('school_report.html')

@app.route('/result', methods=['POST'])
def results():
    try:
        result = process_behaviour(request.form)
        result_title = 'Mental analysis result'
    except Exception as e:
        return render_template('school_report.html')
    else:
        return render_template('report.html', result_title=result_title, result=result)


@app.route('/signin', methods=['GET'])
def signin():
    return render_template('login.html')

@app.route('/session', methods=['GET'])
def session():
    return render_template('session.html')


def process_form(data):
    details = []
    form_tags = [f'q{x}' for x in range(1, 19)]
    for idx in data.keys():
        if idx in form_tags:
            val = option_dict.get(int(data[idx][-1]))
            details.append(val.lower())
    
    return details

def get_completion(data):
    pred = data['prediction']
    behaviour = data['behaviour']

    content = f"""The standard ADHD questionnaire had been administered, and the result is predicted to be <{pred.upper()}> \
                and the behavioural pattern of the child is ({behaviour}). Analyze the behaviour in relation to the prediction
                 and ascertain if the prediction is correct. You are to respond with a YES if the prediction \
                is correct or NO if not. You are to strictly respond only with a Yes or a No"""
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Mental health assistant"},
            {"role": "user", 
             "content": content}
            ]
        )
    return resp.choices[0].message.content

def process_behaviour(data):
    global prediction_data
    detail = []
    behaviour = data.get('additionalInfo', '')
    if behaviour:
        prediction_data['behaviour'] = behaviour
        result = get_completion(prediction_data)
        pred = prediction_data['prediction']
        confidence_level = prediction_data['confidence level']

        if result.lower() == 'yes':
            response = f"""Given the behavioural report ({behaviour}), \
                the MIS predicts that the child has {pred.upper()}, with a confidence level of {confidence_level}%. \nSpeak to a consultant using 
                the link below."""
        else:
            response = f"""Given the behavioural report ({behaviour}), \
                the MIS recommends you book a session with a specialist. \nSpeak to a consultant using 
                the link below."""
            
        return response
    return ''

if __name__ == "__main__":
    app.run(debug=True)