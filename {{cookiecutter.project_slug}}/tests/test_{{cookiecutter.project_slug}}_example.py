from {{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}
import unittest
from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.getOrCreate()

class example_test(unittest.TestCase):
    # Test that the returned DataFrame has the right value(s)
    def test_example_returns_expected(self):
        string = {{cookiecutter.project_slug}}.example("Example Called")
        self.assertEqual(string, "Example Called")
