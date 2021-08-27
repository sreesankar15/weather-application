from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)
app.secret_key = '5#y2L"F4Q8z\n\xec]/we666r)g@5f_'

API_key = '3ad8d453eb5a8c14d8a919236404e7ec'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        city = request.form['city'].capitalize()
        API_KEY = '3ad8d453eb5a8c14d8a919236404e7ec'

        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?&appid={API_key}&q={city}&units=metric')

        weather_data = weather_url.json()

        try:
            temp = round(weather_data['main']['temp'],2)
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
        except KeyError:
            flash('Sorry, an error ocurred. Please try again.', category='error')
            return render_template('index.html')

        return render_template("results.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)

    return render_template('index.html')
if __name__ == '__main__':
    app.run()