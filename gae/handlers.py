import webapp2

url = 'http://grooveshark.com'
html5_url = 'http://html5.grooveshark.com'
import urllib2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #if not self.request.headers.get('Origin'):
        #    return self.response.out.write('')
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        
        #proxy = urllib2.ProxyHandler({'http': 'IP:PORT'})
        #opener = urllib2.build_opener(proxy)
        
        opener = urllib2.build_opener()
        urllib2.install_opener(opener)
        
        # submit the client headers, so that the request isn't denied
        for h in ['User-Agent', 'Accept-Language', 'Accept']:
            opener.addheaders = [(h, str(self.request.headers[h]))]

        conn = urllib2.urlopen(html5_url if self.request.get('html5') == "true" else url)
        html = conn.read()

        self.response.out.write(html)
