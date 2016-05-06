
from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import pymysql
import pycurl
import sys
import cStringIO
import json
import time
from kik.messages import messages_from_json, TextMessage
from kik import KikApi, Configuration

class Message(tornado.web.RequestHandler):

        def get(self):
                print("get")
	def post(self):
#data_json = tornado.escape.json_decode(self.request.body)
#		if not kik.verify_signature(self.request.headers.get('X-Kik-Signature'), self.request.get_data()):
#			return Response(status=403)
		#print data
		#try:
		#	json_data = json.loads(data)
		#except ValueError:
		#	raise tornado.httpserver._BadRequestException("Invalid JSON structure.")
        	#if type(json_data) != dict:
		#	raise tornado.httpserver._BadRequestException("We only accept key value objects!")
		#for key, value in json_data.iteritems():
            	#	self.request.arguments[key] = [value,]
        	#self.done()
		data_json = tornado.escape.json_decode(self.request.body)
		messages = messages_from_json(data_json["messages"])
		for message in messages:
        		if isinstance(message, TextMessage):
				kik.send_messages([
				TextMessage(
					to=message.from_user,
					chat_id=message.chat_id,
					body=message.body
				)])





		#data_json = tornado.escape.json_decode(self.request.body)

		
		print(data_json)

		#kik.send_messages([
		#	TextMessage(to="lea.is.the.bomb10", chat_id="lea.is.the.bomb10", body="no hr violation here")
		#
		response = { 'cohort': "yo" }
		self.write(response)

kik = KikApi("moddtestbot", "5bef24c1-00c1-44bb-a0bc-28b3ed2148fb")
kik.set_configuration(Configuration(webhook="http://159.203.220.30:8889/kik"))


application = tornado.web.Application([(r"/kik", Message)])
if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()




