from courses_app.serializers import CourseSerializer
from django.test import TestCase, Client
from courses_app.models import *
from django.urls import reverse
from rest_framework import status
from rest_framework.utils import json


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="English",
            imgpath="http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg"
        )


    def test_category_imgpath(self):
        english = Category.objects.get(name="English")
        self.assertEqual(english.imgpath, 'http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg')


class BranchTestCase(TestCase):
    def course(name='Name'):
        return Course.objects.create(name=name)

    def setUp(self):
        self.branch = Branch.objects.create(
            course=self.course(),
            latitude='latitude',
            longitude='longitude',
            address='address'
        )

    def test_branch(self):
        branch = Branch.objects.get(name='Branch', latitude='latitude', longitude='longitude', address='address')
        self.assertEqual(branch.address, 'address')


class CourseTestCase(TestCase):
    def create_category(name="English", imgpath="ImgPath"):
        return Category.objects.create(name=name, imgpath=imgpath)

    def setUp(self):
        self.category = self.create_category()
        Course.objects.create(
            name='English',
            description='Миссия English Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.',
            category=self.category,
            logo='Logo'
        )

    def test_course_category(self):
        english = Course.objects.get(name='English')
        self.assertEqual(english.category_id, 1)




# initializing the APIClient app
client = Client()

class CreateNewCourse(TestCase):
    """ Test module for inserting a course"""

    def setUp(self):
        self.valid_payload = {
            'name': 'Name',
            'discription': 'discription',
            'category': 'Category',
            'logo': 'logo'

        }
        self.invalid_payload = {
            'name': '',
            'discription': 'none',
            'category': 'none',
            'logo': 'logo'
        }

    def test_create_valid_course(self):
        response = client.post(
            reverse('get_post_course'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_course(self):
        response = client.post(
            reverse('get_post_course'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateCourseTest(TestCase):
    """ Test module for updating an existing course """

    def setUp(self):
        self.course = Course.objects.create(
            name='name', category='category', description='description', logo='logo')
        self.valid_payload = {
            'name': 'Name',
            'discription': 'discription',
            'category': 'Category',
            'logo': 'logo'

        }
        self.invalid_payload = {
            'name': '',
            'discription': 'none',
            'category': 'none',
            'logo': 'logo'
        }
    def test_valid_update_course(self):
        response = client.put(
            reverse('get_delete_update_course', kwargs={'pk': self.course.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_course(self):
        response = client.put(
            reverse('get_delete_update_course', kwargs={'pk': self.course.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetSingleCourseTest(TestCase):
    """ Test module for GET single courses API """

    def setUp(self):
        self.course = Course.objects.create(
            name='name', category='category', description='description', logo='logo')
        self.course = Course.objects.create(
            name='name', category='category', description='description', logo='logo')
        self.course = Course.objects.create(
            name='name', category='category', description='description', logo='logo')
        self.course = Course.objects.create(
            name='name', category='category', description='description', logo='logo')

    def test_get_valid_single_course(self):
        response = client.get(
            reverse('get_delete_update_course', kwargs={'pk': self.course.pk}))
        course = Course.objects.get(pk=self.rambo.pk)
        serializer = CourseSerializer(course)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_course(self):
        response = client.get(
            reverse('get_delete_update_course', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

