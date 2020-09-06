from utilities.service_utils import ServiceUtility
import pytest
import unittest
import jsonpath


class WebServiceTests(unittest.TestCase):
    serviceUtils = ServiceUtility('https://reqres.in/')

    @pytest.mark.run(order=0)
    def test_create_user(self):
        json_file_path = self.serviceUtils.get_file_from_resources('CreateUser.json')
        request_json = self.serviceUtils.read_file_as_json(json_file_path)
        post_response = self.serviceUtils.make_post_request('api/users', request_json)
        self.serviceUtils.print_response_details()
        self.assertEqual(post_response.status_code, 201)
        response_as_json = post_response.json()
        self.assertEqual(request_json['name'], response_as_json['name'], 'matching name:')
        self.assertEqual(request_json['job'], response_as_json['job'], 'matching job title:')
        name_from_response = jsonpath.jsonpath(post_response.json(), 'name')
        job_from_response = jsonpath.jsonpath(post_response.json(), 'job')
        self.assertEqual(request_json['name'], name_from_response[0], 'matching name:')
        self.assertEqual(request_json['job'], job_from_response[0], 'matching job title:')

    @pytest.mark.run(order=1)
    def test_get_users_page_2(self):
        get_response = self.serviceUtils.make_get_request('api/users?page=2')
        self.serviceUtils.print_response_details()
        self.assertEqual(get_response.status_code, 200, 'matching status code:')
        data_from_response = jsonpath.jsonpath(get_response.json(), 'page')
        self.assertEqual(data_from_response[0], 2, 'matching page number:')
        first_email = jsonpath.jsonpath(get_response.json(), 'data[0].email')
        self.assertEqual(first_email[0], 'michael.lawson@reqres.in', 'matching email:')
        first_name = jsonpath.jsonpath(get_response.json(), 'data[0].first_name')
        self.assertEqual(first_name[0], 'Michael', 'matching first name:')
