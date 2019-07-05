
from .models.serializers import *
import unittest

from django.test import Client



class test_course(unittest.TestCase):
    url = 'course'
    def test_setUp(self):
        self.client = Client()
        print(self.client)

        def test_create_todo(self):
            response = self.client.post(self.url, {
                "name": "English Zone",
                "description": "Миссия English Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.",
                "category": 6,
                "logo": "http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg",
                "contacts": [
                    {
                        "type": 1,
                        "value": "0770 792 299"
                    },
                    {
                        "type": 2,
                        "value": "https://www.facebook.com/english.zone.kg/"
                    },
                    {
                        "type": 3,
                        "value": "ezone.kg@gmail.com"
                    }
                ],
                "branches": [
                    {
                        "address": "Manas 58/ Aini - right next to the Manas university",
                        "latitude": "42.847971",
                        "longitude": "74.586733"
                    },
                    {
                        "address": "Бишкек, Юг-2 дом 15а Советская/Горького",
                        "latitude": "42.8586017",
                        "longitude": "74.6068425"
                    }
                ]
            })
            self.assertEqual(response.status_code, 201)

        def test_details(self):
            response = self.client.get('/course/78/')
            self.assertEqual(response.status_code, 200)

        def test_not_found(self):
            response = self.client.get('/course/1/')
            self.assertEqual(response.status_code, 404)



