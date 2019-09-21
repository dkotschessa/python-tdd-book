from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # edith has heard about a cool new to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # there is still a text box for another item
        # she enters "User peackock feathers to make a fly"

        # the page updates again showing both items

        # she sees the site has generated a unique URL
        # there is some explanatory text to that effect

        # she visits that URL - her to do list is still there

        # satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
