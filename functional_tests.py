from selenium import webdriver

browser = webdriver.Firefox()
# edith has heard about a cool new to-do app. She goes
# to check out its homepage
browser.get('http://localhost:8000')

# she notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# she is invited to enter them straight away

# she types "buy peackock feathers" into a text box (she likes
# fly tying)

# she hits enter and the page lists
# "1: buy peackock feathers" as a to do

# there is still a text box for another item
# she enters "User peackock feathers to make a fly"

# the page updates again showing both items

# she sees the site has generated a unique URL
# there is some explanatory text to that effect

# she visits that URL - her to do list is still there

# satisfied, she goes back to sleep

browser.quit()

