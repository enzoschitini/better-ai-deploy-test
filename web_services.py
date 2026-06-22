from src.web_services_network.api import WebServiceAPI

web_service = WebServiceAPI()

app = web_service.initialize()

# uvicorn web_services:app --reload