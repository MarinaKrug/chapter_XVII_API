import unittest
import python_repos

class PythonRepostestCase(unittest.TestCase):
    """тестирование  python_repos.py"""

    def test_status_code_200(self):
        """значение status_code равно 200"""
        result = python_repos.r.status_code
        self.assertEqual(result, 200)

    def test_total_repo_count(self):
        """Общее количество репозиториев превышает порог в 500 шт."""
        result = (python_repos.response_dict['total_count']) > 500
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
