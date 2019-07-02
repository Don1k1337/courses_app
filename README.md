# courses_app
FORMAT: 1A

# Courses API 

This API helps users register and view a specific course

## Courses Collection [/courses]

### List All Questions [GET]

+ Response 200 (application/json)

{
            "id": 6,
            "name": "English Zone",
            "description": "Миссия English Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.",
            "category": “Language courses”,
            "logo": "http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg",
            "contacts": [
        {
            "type": "PHONE",
            "value": "0770 792 299"
        },
        
            "type": "FACEBOOK",
            "value": "https://www.facebook.com/english.zone.kg/"
        },
        {
            "type": "EMAIL",
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
}


### Create a New Course [POST]

If you want, you can create your own course using this action in the API. It takes an object that contains the JSON in which the course is placed.

+ Request (application/json)

{
    "name": "Language courses",
    "description": "",
    "category": 1,
    "logo": "Logotype",
    "contacts": [
        {
            "type": "PHONE",
            "value": "0770 792 299"
        },
        
            "type": "FACEBOOK",
            "value": "https://www.facebook.com/english.zone.kg/"
        },
        {
            "type": "EMAIL",
            "value": "ezone.kg@gmail.com"
        }
    ],

    "branches": [
    {
            "address": "Бишкек, Юг-2 дом 15а Советская/Горького",
            "latitude": "42.8586017",
            "longitude": "74.6068425"
        
    
}
