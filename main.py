from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


class Common(webapp.RequestHandler):
    
    def render(self, template_html, values={}):
        renderd = template.render(template_html, values)
        self.response.out.write(renderd)
        return


class MainPage(Common):
    
    def get(self):
        self.render("./templates/main.html")


application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
