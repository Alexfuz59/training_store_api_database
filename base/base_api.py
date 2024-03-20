import allure
import json
from allure_commons.types import AttachmentType


class BaseAPI:
    response = None
    response_json = None
    parsed_object = None
    SCHEMA = None

    @allure.step('Response validation')
    def validate_scheme(self):
        parsed_object = self.SCHEMA.model_validate(self.response_json)
        return parsed_object

    @allure.step('Check response is 200')
    def check_response_is_200(self):
        assert self.response.status_code == 200, f'Error status code {self.response.status_code}'

    @allure.step('Add json to allure report')
    def attach_response(self):
        response = json.dumps(self.response_json, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)