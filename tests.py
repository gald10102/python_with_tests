import unittest
from unittest.mock import patch
from main import get_status_code

class TestMain(unittest.TestCase):

    @patch('requests.get')
    def test_get_status_code_success(self, mock_get):
        # הגדרת Mock לתגובה של הבקשה
        mock_get.return_value.status_code = 200
        
        result = get_status_code('https://example.com')
        self.assertEqual(result, 200)

    @patch('requests.get')
    def test_get_status_code_failure(self, mock_get): #dsad
        # הגדרת Mock שמחזיר שגיאה
        mock_get.side_effect = requests.exceptions.RequestException("Network error")
        
        result = get_status_code('https://example.com')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
