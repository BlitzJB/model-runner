from flask import request

def call_model(*inputs):
    return 'FILLER OUTPUT'


def parse_request():
    form = request.form
    return call_model(form)
