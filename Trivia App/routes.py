from flask import Flask, url_for;
from app import app;

#Server/
@app.route('/')
def hello():
    """Renders a sample page."""
    createlink = "<a href='" + url_for('create') + "'>Create Page</a>" #'create' refers to the function name not the route
    return """
            <html>
                <head>
                    <title>Hello World!</title>
                </head>
                <body>
                    <h1>Hello, friend. Hello, friend? That's lame. Maybe I should give you a name :P <h1>
                    """ + createlink + """
                </body>
            </html>""";

#Server/create
@app.route('/create')
def create():
    if request.method == 'GET':
        #send the form to the user
        return render_template('CreateQuestion');
    elif request.method == 'POST':
        #read data from the form and save it to database
        title = request.form['title'];
        question = request.form['question'];
        answer = request.form['answer'];
        #store the above data in a database
        return render_template('CreatedQuestion.html', question=question);
    else:
        return "<h2>Invalid request</h2>";

#Server/question
@app.route('/question/<title>')
def question(title):
    return "<h2>Hey " + title + "</h2>"