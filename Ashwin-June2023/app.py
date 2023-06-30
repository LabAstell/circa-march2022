from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/magnified/<filename>')
def magnified(filename):
    return render_template('magnified.html', image=filename)

@app.route('/entertainment')
def entertainment():
    return render_template('entertainment.html')

@app.route('/going-places')
def going_places():
    return render_template('going_places.html')

@app.route('/home_community_life')
def home_community_life():
    return render_template('home_community_life.html')

@app.route('/people_events')
def people_events():
    return render_template('people_events.html')

@app.route('/sports_recreation')
def sports_recreation():
    return render_template('sports_recreation.html')

@app.route('/working_life')
def working_life():
    return render_template('working_life.html')

@app.route('/childhood')
def childhood():
    return render_template('childhood.html')

if __name__ == '__main__':
    app.run()
