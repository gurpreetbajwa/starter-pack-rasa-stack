# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_processfile"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
#        request = json.loads(
#            requests.get("https://api.chucknorris.io/jokes/random").text
#        )  # make an api call
#        joke = request["value"]  # extract a joke from returned json response
        filename = tracker.get_slot('filename')
        file_prefix = "chatbot"
        full_path = file_prefix + "/" + filename
#       dispatcher.utter_message("The full path of you file is: " + full_path)  # send the message back to the user
        with open('sample.xlsx', 'rb') as f:
            r = requests.post('http://httpbin.org/post', files={'sample.xlsx': f})
        dispatcher.utter_message(r.text)
        return []
