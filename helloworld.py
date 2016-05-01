import webapp2
import os
import jinja2

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('homepage.html')
        context = {}
        self.response.out.write(template.render(context))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
