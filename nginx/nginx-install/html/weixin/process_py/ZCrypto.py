import time
from flask import Flask,g,request,make_response
import hashlib
import xml.etree.ElementTree as ET
from flup.server.fcgi import WSGIServer

app = Flask(__name__)
app.debug=True

@app.route('/',methods=['GET','POST'])
def wechat_auth():
	if request.method == 'GET':
		token='crypto'
		data=request.args
		signature=data.get('signature','')
		timestamp=data.get('timestamp','')
		nonce=data.get('nonce','')
		echostr=data.get('echostr','')
		s=[timestamp,nonce,token]
		s.sort()
		s=''.join(s)
		if(hashlib.sha1(s).hexdigest() == signature):
			return make_response(echostr)
	else:
		rec = request.stream.read()
		xml_rec = ET.fromstring(rec)
		tou = xml_rec.find('ToUserName').text
		fromu = xml_rec.find('FromUserName').text
		content = xml_rec.find('Content').text
		response = make_response(xml_rep%(fromu, tou,  str(int(time.time())), content))
		response.content_type='application/xml'
		return response
	return 'Hello weixin'

if __name__ == '__main__':
    WSGIServer(app, bindAddress='127.0.0.1', 49999).run()
#from bae.core.wsgi import WSGIApplication
#application = WSGIApplication(app)