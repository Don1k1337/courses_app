FORMAT: 1A

HOST: https://github.com/Don1k1337/courses_app/

# courses_app API

The mission of courses is to help people unleash thier full potential and improve their knowledge

### Set-Up Instructions ###

Create a virtual environment to isolate our package dependencies locally

'$ python3 -m venv env'

`$ source env/bin/activate`

On Windows use `$ env\Scripts\activate'

`$ pip3 install -r requirements.txt`

`$ python3 manage.py migrate`

`$ python3 manage.py runserver `

# Group Courses

## Courses Collection [/courses]

### Get All Courses [GET /courses]
+ Response 200 (application/json)
  + Attributes
    - courses (array[Course])
      
        
### Get Individual Course [GET /course/id]
+ Parameter
  + id: `1` - The ID of the course
  
+ Response 200 (application/json)
  + attributes
    - Include Course
    
# Data Structures

## Course (object)
- id: `1` (number) - The ID of the course
- name: `English Zone` (string) - The title of the course
- description: `Миссия English Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.` (string) - The description of the course
- category: `Language courses` (string) - The category of the courses
- logo: `http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg` (string) - Logo of the course
- contacts (array[Contacts]) 
- branches (array[Branches])
  
### Contacts (object)
- type: `1` (number) - The contact type
- value: `0770 792 299` (number) - The contact value
- type: `2` (number) - The contact type
- value: `https://www.facebook.com/english.zone.kg/` (text) - The contact value
- type: `3` (number) - The contact type
- value: `ezone.kg@gmail.com` (text) - The contact value

### Branches (object)
- address: `Manas 58/ Aini - right next to the Manas university` (text) - Address of course
- latitude: `42.847971` (number) - Cordinates of course
- longitude: `74.586733` (number) - Cordinates of course
