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


import re
import requests
import json


class Chelicera:
    def __init__(self, url):
        self.url = url

    def make_get_words(self, target_word):
        word = str(target_word)
        response = requests.get(self.url)

        if response.status_code == 200:
            
            occurrences = re.findall(word, response.text, flags=re.IGNORECASE)

            for occurrence in occurrences:
                print(f'Occurrence of the word "{target_word}": {occurrence.start()}')
        else:
            print(f"Request failed with status code {response.status_code}")

        
            
    def make_get_links(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            links = re.findall(r'<a href="(.*?)".*?>(.*?)</a>', response.text)

            for link in links:
                url, text = link
                print(f'Link: {url} - Text: {text}')
        else:
            print(f"Request failed with status code {response.status_code}")
                