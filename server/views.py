from .app import app
from model.call import parse_request


@app.route('/process_survey_response')
def _process_survey_response():
    return parse_request()