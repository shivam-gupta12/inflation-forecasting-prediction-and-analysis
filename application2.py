import io
import base64
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import pickle
from datetime import datetime
from statsmodels.tsa.statespace.sarimax import SARIMAXResults

application2 = Flask(__name__)
app = application2

def load_model(category):
    # Load the SARIMAX model from the file
    model_path = f"models/{category.replace(' ', '_')}_model.pkl"
    return SARIMAXResults.load(model_path)

# Function to generate a forecast using the loaded model
def generate_forecast(category, start_date, end_date):
    # Load the model for the specified category
    model = load_model(category)
    
    # Assuming you have a DataFrame or other data source for generating the forecast
    # Here we'll create a DataFrame with a date range between start_date and end_date
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    forecast_data = pd.DataFrame(index=date_range)
    
    # Generate the forecast
    forecast_result = model.predict(start=start_date, end=end_date)
    
    # Add the forecast values to the result dictionary
    forecast_result['forecast_values'] = forecast_result.tolist()
    
    return forecast_result

# Route to render the form
@app.route('/')
def index():
    return render_template('forecast_form.html')

# Route to handle form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get the form data
    category = request.form['category']
    start_date = request.form['start_date']
    print(start_date)
    end_date = request.form['end_date']
    print(end_date)
    
    # Do something with the form data, like generate a forecast
    forecast_result = generate_forecast(category, start_date, end_date)
    print(forecast_result)

    return render_template('forecast_result.html', forecast_result=forecast_result, category=category, 
                           start_date=start_date, 
                           end_date=end_date)


if __name__ == '__main__':
    app.run(debug=True)
    

    

