# Import necessary modules and libraries
from flask import Flask, render_template, request, redirect, url_for

# Create an instance of the Flask web application
app = Flask(__name__)

# Define routes and views
@app.route('/')
def index():
    return 'Hello, World!'

# Example route with dynamic content
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

# Example route that handles form submissions
@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form['data']
        # Process the submitted data here
        return f'You submitted: {data}'
    return render_template('form.html')

# Run the application if this file is executed
if __name__ == '__main__':
    app.run(debug=True)

app.run(host='0.0.0.0', port=9002)

