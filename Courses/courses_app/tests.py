
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
    def course(name='English', description='description', category='Category', logo='logo'):
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
    def create_category(name="English", imgpath="ImgPath"):
        return Category.objects.create(name=name, imgpath=imgpath)

    def setUp(self):
        self.category = self.create_category()
        Course.objects.create(
            name='English',
            description='Миссия English Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.',
            category_id=self.create_category().id,
            logo='Logo'
        )

    def test_course_category(self):
        english = Course.objects.get(name='English')
        self.assertEqual(english.category_id, 2)


class ContactTestCase(TestCase):
    def setUp(self):
        self.courses = Course.objects.create(
            name='Name', discription='discription', category='Category', logo='default.jpg'
        )

    def test_Courses(self):
        Courses_get = Course.objects.get(
            name='Name', discription='discription', category='Category', logo='default.jpg')
        self.assertEqual(Courses_get, self.courses)

