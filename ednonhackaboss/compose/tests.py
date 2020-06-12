from django.test import TestCase
from compose.models import Compose
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

class ComposeTestCase(TestCase):

    def test_create_compose(self):
        compose = Compose.objects.create(name="MyCompose", yaml="MyYamlContent")
        self.assertEquals(compose.name, "MyCompose")
        self.assertEquals(compose.yaml, "MyYamlContent")

    def test_create_compose_without_name_and_yaml(self):
        with self.assertRaises(ValidationError) as context:
            compose = Compose.objects.create()
            compose.clean_fields()
    
    def test_create_compose_without_name(self):
        with self.assertRaises(ValidationError) as context:
            compose = Compose.objects.create(yaml='yaml')
            compose.clean_fields()

    def test_create_compose_without_yaml(self):
        with self.assertRaises(ValidationError) as context:
            compose = Compose.objects.create(name='name')
            compose.clean_fields()
    
    def test_create_compose_with_existing_name(self):
        compose = Compose.objects.create(name='name')
        with self.assertRaises(IntegrityError) as context:
            compose2 = Compose.objects.create(name='name')