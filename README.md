# Mission_to_Mars Web Scraping project

### Mission:
* This project uses MongoDB(Flask_pymongo), Heroku, Flask, pandas, requests, BeautifulSoup, splinter, and selenium webdriver to scrape data on Mars.
* Scrapes news title and paragraph text from most recent story at https://mars.nasa.gov/news/.
* Then uses the web driver to scrape image urls from JPL Nasa website.
* Scrapes Mars weather from https://twitter.com/marswxreport?lang=en.
* Finally, the app uses pandas html feature to scrape a Mars data table. 


### Run without Heroku:
1. Copy/gather the files in this repo (don't need the .gitignore).
2. Start a MongoDB daemon in the terminal, then start mongo instance.
3. Run the app.py in the terminal. Copy the local url to your web browser.
