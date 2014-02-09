import webapp2

url = 'http://grooveshark.com'
html5_url = 'http://grooveshark.com'
import urllib2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #if not self.request.headers.get('Origin'):
        #    return self.response.out.write('')
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

        conn = urllib2.urlopen(html5_url if self.request.get('html5') == "true" else url)
        html = conn.read()

        self.response.out.write(html)
