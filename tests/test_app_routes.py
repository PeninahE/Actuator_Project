#test_app_routes.py

def test_hello(client):
    response = client.get("/hello")
    assert b"hello world" in response.data
def test_app_html(client):
    response = client.get("/")
    assert b"Welcome to my project!" in response.data


def test_actuator_health(client):
    actuator_response = client.post('/actuator', data={'status': 'health'})
    assert b"UP" in actuator_response.data


def test_actuator_env(client):
    actuator_response = client.post('/actuator', data={'status': 'env'})
    assert b"activeProfiles" in actuator_response.data
    assert b"propertySources" in actuator_response.data
    assert b"systemEnvironment" in actuator_response.data


def test_actuator_metrics(client):
    actuator_response = client.post('/actuator', data={'status': 'metrics'})
    assert b"names" in actuator_response.data


def test_actuator_logfile(client):
    actuator_response = client.post('/actuator', data={'status': 'logfile'})
    assert b"t_admin_registration" in actuator_response.data


def test_actuator_httptrace(client):
    actuator_response = client.post('/actuator', data={'status': 'httptrace'})
    assert b"timestamp" in actuator_response.data
    assert b"sec-fetch-mode" in actuator_response.data
    assert b"accept-encoding" in actuator_response.data


def test_actuator_threaddump(client):
    actuator_response = client.post('/actuator', data={'status': 'threaddump'})
    assert b"MainThread" in actuator_response.data
    assert b"lineNumber" in actuator_response.data
    assert b"threadId" in actuator_response.data
