from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, request
from selenium.webdriver.chrome.service import Service

app = Flask(__name__, template_folder='Template')


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/automation", methods=['Get', 'POST'])
def run_automation():
    if request.method == 'POST':
        search_key = request.form.get('search_key')
        title = selenium_code(search_key)
        return title


def selenium_code(search_key):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://www.google.com")
    driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys(search_key)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').submit()
    title = driver.title
    driver.quit()
    return title


if __name__ == "__main__":
    app.run(debug=True)
