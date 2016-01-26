"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Survey(Controller):
    def __init__(self, action):
        super(Survey, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        return self.load_view('index.html')

    def process(self):
        try:
            if not (session['count']):
                session['count'] = 1
            else:
                session['count'] += 1
            name = request.form['name']
            comment = request.form['comment']
            if len(name) > 0 and name.isalpha():
                session['name'] = name
            else:
                flash("Name cannot be blank or have numbers.")
            if len(comment) > 0:
                session['comment'] = comment
            else:
                flash("Comment cannot be blank.")

            session['location'] = request.form['location']
            session['language'] = request.form['language']
            return redirect('/survey/result')
        except:
            return redirect('/')

    def result(self):
        return self.load_view('result.html')


