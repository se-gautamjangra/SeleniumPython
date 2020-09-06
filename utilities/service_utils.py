import requests
import json
import os


class ServiceUtility():

    def __init__(self,base_url):
        self.response = 'no response yet'
        self.base_url = base_url

    def make_get_request(self, relative_url):
        print('************* Sending GET Request *************')
        request_url = self.base_url + relative_url
        self.response = requests.get(request_url)
        return self.response

    def make_post_request(self, relative_url, request_json):
        print('************* Sending POST Request *************')
        request_url = self.base_url + relative_url
        self.response = requests.post(request_url, request_json)
        return self.response

    def make_put_request(self, relative_url, request_json):
        print('************* Sending POST Request *************')
        request_url = base_url + relative_url
        self.response = requests.put(request_url, request_json)
        return self.response

    def get_response_body_as_json(self):
        return json.loads(self.response.text)

    def get_response_code(self):
        return self.response.status_code

    def get_response_cookies(self):
        return self.response.cookies

    def get_response_headers(self):
        return self.response.headers

    def print_response_details(self):
        response = self.response
        print('Response body -> ')
        print(self.get_response_body_as_json())
        print('Response code -> ')
        print(self.get_response_code())

    def read_file_as_json(self, file_path):
        file = open(file_path, 'r')
        file_data = file.read()
        json_data = json.loads(file_data)
        file.close()
        return json_data

    def get_file_from_resources(self, relative_file_path):
        dir_name = os.getcwd()
        file_path = dir_name + '\\resources\\' + relative_file_path
        return file_path

