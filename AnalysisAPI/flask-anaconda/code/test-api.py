#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import single_keyword_classification
import json

app = FlaskAPI(__name__)

notes = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
    3: 'eiei',
}

def note_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': notes[key]
    }


@app.route("/phone", methods=['POST'])
def notes_list():
    print json.dumps(request.json)
    if not request.json or not 'input' in request.json:
        return {
                    'status':'400',
                    'message':'Input is missing'    
                }

    result = single_keyword_classification.run({
        'input': request.json['input']
    })
    # print json.dumps(result, sort_keys=False)
    return result

    # request.method == 'GET'
    # return [note_repr(idx) for idx in sorted(notes.keys())]


# @app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
# def notes_detail(key):
#     """
#     Retrieve, update or delete note instances.
#     """
#     if request.method == 'PUT':
#         note = str(request.data.get('text', ''))
#         notes[key] = note
#         return note_repr(key)

#     elif request.method == 'DELETE':
#         notes.pop(key, None)
#         return '', status.HTTP_204_NO_CONTENT

#     # request.method == 'GET'
#     if key not in notes:
#         raise exceptions.NotFound()
#     result = single_keyword_classification.run({
#         'input': {
#             'type': 'phone',
#             'value': '02-105-6234',
#         }
#     })
#     # print json.dumps(result, sort_keys=False)
#     return result


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')