"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request, url_for
from flask_restplus import Api
import os
import random



from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest
import logging

from werkzeug.utils import secure_filename


import json
from . import hmm
from .spellchecker import checkParagraph, _head





@api_rest.route('/hmm')
class Hmm(BaseResource):
    def post(self):
        data = json.loads(request.data)
        return {'status': 'OK', 'tags': hmm.findtags(data['text'])}


@api_rest.route('/checker')
class SpellChecker(BaseResource):
    def get(self):
        return {'status': 'OK'}

    def post(self):
        data = json.loads(request.data)
        return {'status': 'OK', 'corrections': checkParagraph(data['text'], _head)}