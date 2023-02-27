import unittest
from pathlib import Path

from extraction import extract_images_from_pdfs

BASE_PATH = Path(__file__).resolve().parent
output_directory = BASE_PATH/"output"
input_directory = BASE_PATH/"input"

class MyTestCase(unittest.TestCase):
    def test_somthing(self):
        extract_images_from_pdfs(str(input_directory), str(output_directory))
        expected_result =["0a3ceb8b-43af-43ef-93d7-5adeb78d6df9.pdf"]
        self.assertEqual(True, False) #Add assertion here

if __name__ =='__main__':
    unittest.main()