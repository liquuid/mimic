from django.test import TestCase

from mimic.core.forms import SubmitText


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
        self.form = SubmitText()

    def test_get(self):
        """
        GET / must return status code 200
        """
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        """Must use index.html """

        self.assertTemplateUsed(self.response, 'index.html')

    def test_has_title_header(self):
        self.assertContains(self.response, "<h2")

    def test_has_title_description(self):
        self.assertContains(self.response, "<h3")

    def test_has_form_label(self):
        self.assertContains(self.response, "<label")

    def test_has_form(self):
        self.assertContains(self.response, "<form")

    def test_has_textarea(self):
        self.assertContains(self.response, "<textarea")

    def test_csrf(self):
        """html must contain {% csrf_token %}"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_bootstrap_css(self):
        self.assertContains(self.response, 'bootstrap.min.css')

    def test_bootstrap_js(self):
        self.assertContains(self.response, 'bootstrap.min.js')

    def test_jquery(self):
        self.assertContains(self.response, 'jquery.min.js')

    def test_has_form(self):
        """context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubmitText)

    def test_input_submit(self):
        """html must contain {% csrf_token %}"""
        self.assertContains(self.response, '<button type="submit"')

    def test_has_blog_link(self):
        self.assertContains(self.response, '<a class="btn btn-success" href="http://liquuid.me" type="link">')

    def test_has_twitter_user(self):
        self.assertContains(self.response, '<a class="btn btn-info" href="https://twitter.com/liquuid" type="link">')

    def test_form_has_fields(self):
        form = self.response.context['form']
        self.assertSequenceEqual(['text',], list(form.fields))

class SubmitTextTest(TestCase):
    def setUp(self):
        self.data = dict(text="mi mi mi")
        self.response = self.client.post('/', self.data)