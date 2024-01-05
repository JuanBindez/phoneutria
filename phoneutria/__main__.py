# this is part of the phoneutria project.
#
# Copyright ©  2024  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,



import requests
import json


class Chelicera:
    def __init__(self, url):
        self.url = url

    def make_get_request(self, extract_data=None):
        try:
            response = requests.get(self.url)
            print(f"GET {self.url} - Status Code: {response.status_code}")
            print(response.text)

            # Verificação de XSS
            if "<script>" in response.text:
                print("Possible XSS detected in response.")

            if extract_data:
                try:
                    response_json = response.json()

                    # Verificação de SQL Injection
                    for key in extract_data:
                        if key in response_json:
                            value = response_json[key]
                            if isinstance(value, str) and "'" in value:
                                print(f"Possible SQL Injection detected in field '{key}'.")

                            print(f"{key}: {value}")
                        else:
                            print(f"Field '{key}' not found in the response.")
                except json.JSONDecodeError as e:
                    
                    print(f"Error decoding JSON response: {e}")
            else:
                print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error making GET request: {e}")

    def make_post_request(self, data):
        try:
            response = requests.post(self.url, data=data)
            print(f"POST {self.surl} - Status Code: {response.status_code}")
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error making POST request: {e}")
