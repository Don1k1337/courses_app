
from django.test import TestCase


from Courses.courses_app.models import Category, Branch, Course


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="English Zone",
            imgpath="http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg"
            )

    def test_category_imgpath(self):
        english = Category.objects.get(name="Language courses")
        self.assertEqual(english.imgpath, '')

class BranchTestCase(TestCase):
    def setUp(self):
        Branch.objects.create(
            course='4',
            latitude='latitude',
            longitude='longitude',
            address='address'
        )

    def test_branch_address(self):
        english = Branch.objects.get(course=self.create_course().id)
        self.assertEqual(english.address, 'address')

class CourseTestCase(TestCase):
    def create_category(name="ExampleName", imgpath="ImgPath"):
        return Category.objects.create(name=name, imgpath=imgpath)

    def setUp(self):
        Course.objects.create(
            name='English Zone',
            description='Миссия English Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.',
            category_id=self.create_category().id,
            logo='Logo'
        )

    def test_course_category(self):
        english = Course.objects.get(name='Language courses')
        self.assertEqual(english.category_id, 6)
