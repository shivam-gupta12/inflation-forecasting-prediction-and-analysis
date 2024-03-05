# # import pickle
# # from flask import Flask,request,jsonify,render_template, send_file
# # import numpy as np
# # import pandas as pd
# # from sklearn.preprocessing import StandardScaler
# # import matplotlib.pyplot as plt

# # application = Flask(__name__)
# # app=application

# # model_fit = pickle.load(open("/Users/damodargupta/Desktop/EPICS-PROJECT/sarimax_model.pkl", "rb"))

# # ## Route for home page
# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # def get_inflation_rate_range(df, start_year, end_year):
# #     df = pd.read_excel("/Users/damodargupta/Desktop/EPICS-PROJECT/inflation_ratings.xlsx")
# #     # Filter the dataframe for the given range of years
# #     df_range = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
# #     # Melt the dataframe to have 'months' and 'inflation ratings' in separate columns
# #     df_melted = df_range.melt(id_vars=['Year'], var_name='Month', value_name='Inflation Rate')
# #     return df_melted

# # @app.route('/predictdata',methods=['GET','POST'])
# # def predict_datapoint():
# #     if request.method=='POST':
# #         start = int(request.form.get('start'))
# #         end = int(request.form.get('end'))
# #         event = float(request.form.get('event'))
# #         if event == "Ukraine-Russia War":
# #             event_list = [(pd.to_datetime('2022-02-24'), 'Start of\nRussian Invasion', 'purple')]
# #         else:
# #             event_list = [ (pd.to_datetime('2023-03-31'), 'Start of\nForecast', 'crimson')]
            
# #         yhat = model_fit.predict(start=start, end=end, typ='levels', dynamic=False).rename('Predict')
        
# #         # forecast and confidence intervals 70% and 95%
# #         conf_int_70 = model_fit.get_forecast(steps=6).summary_frame(alpha=0.3)
# #         conf_int_95 = model_fit.get_forecast(steps=6).summary_frame(alpha=0.05)
        
# #         # extract index list
# #         def index_list():
# #             conf_interval = conf_int_95.reset_index()
# #             return conf_interval['index'].to_list()

# #         indx_list = index_list()

# #         # plot events
# #         for date_point, label, clr in event_list:
# #             plt.axvline(x=date_point, color=clr, linestyle=':')
# #             plt.text(x=date_point, y=23, s=label, horizontalalignment='center', verticalalignment='center',
# #                     color=clr, bbox=dict(facecolor='white', alpha=0.9, boxstyle='round, pad=1', linewidth=0.2))
            
# #         df = pd.read_excel("/Users/damodargupta/Desktop/EPICS-PROJECT/inflation_ratings.xlsx")
# #         inflation_rate_range_df = get_inflation_rate_range(df, start, end)
# #         series = inflation_rate_range_df["Inflation Rate"].head()
        
# #         # 2nd plot - forecasting results
# #         series.plot(legend=True, label='Actual', figsize=(16, 6), color='orange')
# #         yhat.plot(legend=True, color='green')
# #         conf_int_95['mean'].plot(legend=True, label='Forecast', color='crimson')
# #         # confidence intervals 95%
# #         plt.fill_between(x=indx_list, y1=conf_int_95['mean_ci_upper'], y2=conf_int_95['mean_ci_lower'],
# #                         alpha=0.4, label='95% Confidence\nInterval', linewidth=0)
# #         # confidence intervals 70%
# #         plt.fill_between(x=indx_list, y1=conf_int_70['mean_ci_upper'], y2=conf_int_70['mean_ci_lower'],
# #                         alpha=0.6, label='70% Confidence\nInterval', linewidth=0)
# #         plt.xlim(['2020-05', '2023-09'])
# #         plt.title('Inflation Forecast: Mar 2023 - Aug 2023')
# #         plt.legend(loc='upper left')
# #         plt.show()

# # if __name__=="__main__":
# #     app.run(host="0.0.0.0" , port=8000)

# import io
# import base64
# from flask import Flask, request, render_template
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('Agg')
# import pickle
# from datetime import datetime

# application = Flask(__name__)
# app = application

# # Replace the path with your actual path
# model_fit = pickle.load(open("/Users/damodargupta/Desktop/EPICS-PROJECT/sarimax_model.pkl", "rb"))

# # ... (your existing functions)

# @app.route('/')
# def index():
#     return render_template('index-2.html')

# def get_inflation_rate_range(df, start, end):
#     dataframe = pd.read_csv("/Users/damodargupta/Desktop/EPICS-PROJECT/date-wise-data.csv")
#     df['Date'] = pd.to_datetime(df['Date'])
#     # Create filtered DataFrame
#     filtered_df = df[(df['Date'] >= start) & (df['Date'] <= end)]
#     plt.plot(filtered_df['Date'], filtered_df['Rate'], marker='o', linestyle='-')

# @app.route('/predictdata', methods=['GET', 'POST'])
# def predict_datapoint():
#     if request.method == 'POST':
#         # Parse date strings to datetime objects
#         start_date = request.form.get('start_date')
#         print(start_date)
#         end_date = request.form.get('end_date')
#         print(end_date)
#         event = request.form.get('event')
#         print(event)

#         if event == "Ukraine-Russia War":
#             event_list = [(pd.to_datetime(start_date), 'Start of\nRussian Invasion', 'purple'), (pd.to_datetime("2022-02-28"), 'Start of\nForecast', 'crimson')]
#             yhat = model_fit.predict(start=pd.to_datetime("2022-02-28"), end=end_date, typ='levels', dynamic=False).rename('Predict')
#             print(event_list)
#         elif event == "Covid 19 Pandemic":
#             event_list = [(pd.to_datetime(start_date), 'Start of\nForecast', 'purple'), (pd.to_datetime("2020-01-31"), 'Start of\nForecast', 'crimson')]
#             yhat = model_fit.predict(start=pd.to_datetime("2020-01-31"), end=end_date, typ='levels', dynamic=False).rename('Predict')
#             print(event_list)
#         else:
#             event_list = [(pd.to_datetime(start_date), 'Start of\nRussian Invasion', 'purple'), (pd.to_datetime(end_date), 'Start of\nForecast', 'crimson')]
#             yhat = model_fit.predict(start=pd.to_datetime("2020-01-31"), end=end_date, typ='levels', dynamic=False).rename('Predict')
            
#         conf_int_70 = model_fit.get_forecast(steps=6).summary_frame(alpha=0.3)
#         conf_int_95 = model_fit.get_forecast(steps=6).summary_frame(alpha=0.05)

#         def index_list():
#             conf_interval = conf_int_95.reset_index()
#             return conf_interval['index'].to_list()

#         indx_list = index_list()
#         plt.figure(figsize=(16, 6))
#         if event== "None":
#             plt.axvline(x=pd.to_datetime("2020-01-31"), color="purple", linestyle=':')
#             plt.text(x=pd.to_datetime("2020-01-31"), y=17, s="Start of Forecast", horizontalalignment='center', verticalalignment='center',
#                     color="crimson", bbox=dict(facecolor='white', alpha=0.9, boxstyle='round, pad=1', linewidth=0.2))
#         else:
#             plt.axvline(x=event_list[1][0], color="purple", linestyle=':')
#             plt.text(x=event_list[1][0], y=17, s="Start of Forecast", horizontalalignment='center', verticalalignment='center',
#                     color="crimson", bbox=dict(facecolor='white', alpha=0.9, boxstyle='round, pad=1', linewidth=0.2))

#         df = pd.read_csv("/Users/damodargupta/Desktop/EPICS-PROJECT/date-wise-data.csv")
#         get_inflation_rate_range(df, start_date, end_date)    
#         yhat.plot(legend=True, color='green')
#         conf_int_95['mean'].plot(legend=True, label='Forecast', color='crimson')
#         plt.fill_between(x=indx_list, y1=conf_int_95['mean_ci_upper'], y2=conf_int_95['mean_ci_lower'],
#                          alpha=0.4, label='95% Confidence\nInterval', linewidth=0)
#         plt.fill_between(x=indx_list, y1=conf_int_70['mean_ci_upper'], y2=conf_int_70['mean_ci_lower'],
#                          alpha=0.6, label='70% Confidence\nInterval', linewidth=0)
#         plt.xlim([start_date, end_date])
#         if event == "Ukraine-Russia War":
#             plt.title(f'Inflation Forecast: 2022-02-28 to {end_date}')
#         elif event == "Covid 19 Pandemic":
#             plt.title(f'Inflation Forecast: 2020-01-31 to {end_date}')
#         else: 
#             plt.title(f'Inflation Forecast: 2020-01-31 to {end_date}')
#         plt.legend(loc='upper left')
#         plt.savefig('/Users/damodargupta/Desktop/EPICS-PROJECT/plot.png', format='png')

#         # Save the plot to BytesIO object
#         plot_img = io.BytesIO()
#         plt.savefig(plot_img, format='png')
#         plot_img.seek(0)

#         # Encode the plot image as base64
#         plot_img_base64 = base64.b64encode(plot_img.getvalue()).decode('utf-8')

#         # Render the template with the plot image
#         return render_template('index-2.html', plot_img_base64=plot_img_base64)

#     else:
#         return render_template('index-2.html')

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000)

import io
import base64
from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import pickle
from datetime import datetime
from statsmodels.tsa.statespace.sarimax import SARIMAXResults

application = Flask(__name__)
app = application

# Replace the path with your actual path
model_fit = pickle.load(open("sarimax_model.pkl", "rb"))

# ... (your existing functions)

@app.route('/')
def index():
    return render_template('index-2.html')

def get_inflation_rate_range(df, start, end):
    dataframe = pd.read_csv("date-wise-data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    # Create filtered DataFrame
    filtered_df = df[(df['Date'] >= start) & (df['Date'] <= end)]
    plt.plot(filtered_df['Date'], filtered_df['Rate'], marker='o', linestyle='-')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Parse date strings to datetime objects
        data = request.json
        start_date = data.get('start-date')
        print(start_date)
        end_date = data.get('end-date')
        print(end_date)
        event = data.get('event')
        print(event)

        if event == "Ukraine-Russia War":
            event_list = [(pd.to_datetime(start_date), 'Start of\nRussian Invasion', 'purple'), (pd.to_datetime("2022-02-28"), 'Start of\nForecast', 'crimson')]
            yhat = model_fit.predict(start=pd.to_datetime("2022-02-28"), end=end_date, typ='levels', dynamic=False).rename('Predict')
            print(event_list)
        elif event == "Covid 19 Pandemic":
            event_list = [(pd.to_datetime(start_date), 'Start of\nForecast', 'purple'), (pd.to_datetime("2020-01-31"), 'Start of\nForecast', 'crimson')]
            yhat = model_fit.predict(start=pd.to_datetime("2020-01-31"), end=end_date, typ='levels', dynamic=False).rename('Predict')
            print(event_list)
        else:
            event_list = [(pd.to_datetime(start_date), 'Start of\nRussian Invasion', 'purple'), (pd.to_datetime(end_date), 'Start of\nForecast', 'crimson')]
            yhat = model_fit.predict(start=pd.to_datetime("2020-01-31"), end=end_date, typ='levels', dynamic=False).rename('Predict')
            
        conf_int_70 = model_fit.get_forecast(steps=6).summary_frame(alpha=0.3)
        conf_int_95 = model_fit.get_forecast(steps=6).summary_frame(alpha=0.05)

        def index_list():
            conf_interval = conf_int_95.reset_index()
            return conf_interval['index'].to_list()

        indx_list = index_list()
        plt.figure(figsize=(10.5,7))
        if event== "None":
            plt.axvline(x=pd.to_datetime("2020-01-31"), color="purple", linestyle=':')
            plt.text(x=pd.to_datetime("2020-01-31"), y=17, s="Start of Forecast", horizontalalignment='center', verticalalignment='center',
                    color="crimson", bbox=dict(facecolor='white', alpha=0.9, boxstyle='round, pad=1', linewidth=0.2))
        else:
            plt.axvline(x=event_list[1][0], color="purple", linestyle=':')
            plt.text(x=event_list[1][0], y=17, s="Start of Forecast", horizontalalignment='center', verticalalignment='center',
                    color="crimson", bbox=dict(facecolor='white', alpha=0.9, boxstyle='round, pad=1', linewidth=0.2))

        df = pd.read_csv("date-wise-data.csv")
        get_inflation_rate_range(df, start_date, end_date)    
        yhat.plot(legend=True, color='green')
        conf_int_95['mean'].plot(legend=True, label='Forecast', color='crimson')
        plt.fill_between(x=indx_list, y1=conf_int_95['mean_ci_upper'], y2=conf_int_95['mean_ci_lower'],
                         alpha=0.4, label='95% Confidence\nInterval', linewidth=0)
        plt.fill_between(x=indx_list, y1=conf_int_70['mean_ci_upper'], y2=conf_int_70['mean_ci_lower'],
                         alpha=0.6, label='70% Confidence\nInterval', linewidth=0)
        plt.xlim([start_date, end_date])
        if event == "Ukraine-Russia War":
            plt.title(f'Inflation Forecast: 2022-02-28 to {end_date}')
        elif event == "Covid 19 Pandemic":
            plt.title(f'Inflation Forecast: 2020-01-31 to {end_date}')
        else: 
            plt.title(f'Inflation Forecast: 2020-01-31 to {end_date}')
        plt.legend(loc='upper left')
        plt.savefig('plot.png', format='png')

        # Save the plot to BytesIO object
        plot_img = io.BytesIO()
        plt.savefig(plot_img, format='png')
        plot_img.seek(0)

        # Encode the plot image as base64
        plot_img_base64 = base64.b64encode(plot_img.getvalue()).decode()
        plt.close()
        

        # Render the template with the plot image
        # return render_template('index-2.html', plot_img_base64=plot_img_base64)
        return jsonify({'plot_img_base64': plot_img_base64})

    else:
        return render_template('index-2.html')
    
@app.route('/about')
def about():
    return render_template('team_members.html')

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

def add_months_to_date_range(start_date, end_date):
    # Generate a date range with monthly frequency
    date_range = pd.date_range(start=start_date, end=end_date, freq='MS').strftime('%Y-%m-%d').tolist()
    return date_range

@app.route('/predictdatacategorical', methods=['GET', 'POST'])
def predictdatacategorical():
    data = request.json  # Get the JSON data sent from the client
    category = data.get('category')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if not all([category, start_date, end_date]):
        # If any of the fields are missing, you can return an error message
        return jsonify({'error': 'Missing data!'}), 400

    # Continue processing the data and generating forecast
    forecast_result = generate_forecast(category, start_date, end_date)
    print(forecast_result)

    # Since you are expecting to render a template, make sure you pass
    # all the required context variables to the template rendering function.
    # Generate the plot
    plt.figure(figsize=(10, 6))
    plt.plot(add_months_to_date_range(start_date=start_date, end_date=end_date), forecast_result['forecast_values'], marker='o', linestyle='-')
    plt.title(f'Forecast from {start_date} to {end_date}')
    plt.xlabel('Date')
    plt.xticks(rotation = 90 ,  fontsize = 5)

    plt.ylabel('Forecast Values')
    
    # Save the plot to a BytesIO object
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    plt.close()
    bytes_image.seek(0)

    # Encode the image to base64 string and decode to UTF-8
    base64_png = base64.b64encode(bytes_image.getvalue()).decode('utf-8')
    
    return jsonify({
        'success': True,
        'data': {
            'forecast_result': forecast_result.tolist(),  # Convert to list
            'image_base64':  base64_png,
            'category': category,
            'start_date': start_date,
            'end_date': end_date
        }
    })


if __name__ == "__main__":
    app.run(debug=True , port=1111)

