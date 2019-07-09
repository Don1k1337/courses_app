
from django.test import TestCase


from courses_app.models import *



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
    def course(name='English', description='description', category='category', logo='logo'):
        return Course.objects.create(name=name)

    def setUp(self):
        self.branch = Branch.objects.create(
            course=self.course(),
            latitude='latitude',
            longitude='longitude',
            address='address'
        )

    def test_branch(self):
        branch = Branch.objects.get(name='Branch')
        self.assertEqual(branch.address, 'address')


class CourseTestCase(TestCase):
    def create_category(name="ExampleName", imgpath="ImgPath"):
        return Category.objects.create(name=name, imgpath=imgpath)

    def setUp(self):
        Course.objects.create(
            name='English',
            description='Миссия English Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.',
            category_id=self.create_category().id,
            logo='Logo'
        )

    def test_course_category(self):
        english = Course.objects.get(name='English')
        self.assertEqual(english.category_id, 1)


class ContactTestCase(TestCase):
    def create_contact(course='Course', type='Phone', value='Value'):
        return Contact.objects.create(course=course, type=type, value=value)

    def setUp(self):
        Contact.objects.create(
            course='Language course',
            type='Phone',
            value='Value'
        )

    def test_contact(self):
        contact = Contact.objects.get(course='English')
        self.assertEqual(contact.type, 'Phone')