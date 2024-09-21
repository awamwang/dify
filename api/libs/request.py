import logging

from requests import Request, Response

log_debug = logging.debug

def log_request(request: Request):
    log_debug('Request URL: %s', request.url)
    if request.data:
        log_debug('Request Data: %s', request.data)

def log_response(response: Response):
    log_debug('Request URL: %s', response.url)
    if response.status_code == 200: return

    log_debug('Response Status Code: %s', response.status_code)
    log_debug('Response Text: %s', response.text)
    json = response.json()
    if json is not None: 
        log_debug('Response JSON: %s', json)