# Modified from http://blog.dantup.com/2010/01/generic-redirection-script-for-google-app-engine

SOCIAL_URL = 'https://twitter.com/RickByers'
GITHUB_URL = 'https://rbyers.github.io'

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail
import webob, urlparse, logging


class MainHandler(webapp.RequestHandler):

	def get(self):
		# Perform redirect
		url = get_redirect_url(self.request.path)
			
		logging.info('Redirecting ' + self.request.url + ' to ' + url);
		self.redirect(url, permanent=True)


def get_redirect_url(path):
    # Redirect the empty URL to my Social URL
    if not path or path == '/':
        return SOCIAL_URL

    # Redirect everything else to GitHub
    return GITHUB_URL + path

application = webapp.WSGIApplication([("/.*", MainHandler)], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
