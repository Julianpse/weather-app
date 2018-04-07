import os

import requests
import json

import tornado.ioloop
import tornado.web
import tornado.log

# from weather import *

from jinja2 import \
 Environment, PackageLoader, select_autoescape

ENV = Environment(
  loader=PackageLoader('myapp', 'templates'),
  autoescape=select_autoescape(['html', 'xml'])
)

class TemplateHandler(tornado.web.RequestHandler):
    def render_template (self, tpl, context):
        template = ENV.get_template(tpl)
        context['page'] = self.request.path
        self.write(template.render(**context))

class MainHandler(TemplateHandler):
    def get(self):
        self.set_header(
            'Cache-Control',
            'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("form.html", {})

class ResultsHandler(TemplateHandler):
    def post(self):
        city_input = self.get_body_argument('city')
        if city_input:
            self.render_template("results.html", {})
        else:
            self.redirect(r"/error")

class ErrorHandler(TemplateHandler):
    def get(self):
        self.set_header(
            'Cache-Control',
            'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("error.html", {})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/results", ResultsHandler),
        (r"/error", ErrorHandler),
        (
          r"/static/(.*)",
          tornado.web.StaticFileHandler,
          {'path': 'static'}
        ),
    ], autoreload=True)

if __name__ == "__main__":
    tornado.log.enable_pretty_logging()

    app = make_app()
    PORT = int('8000')
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
