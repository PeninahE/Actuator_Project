#test_ServiceCaller.py

from actuator.services import ServiceCaller


def test_call_service():
    service_url = "http://127.0.0.1:8000/pyctuator/health"

    service_caller = ServiceCaller(service_url)
    json_response = service_caller.call_service()

    # add other relevant tests
    assert json_response
    assert service_caller.json_response == json_response