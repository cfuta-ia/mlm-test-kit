from framework.util import webdriver
from framework.element import element

url = "http://localhost:8188/data/perspective/client/MachineLearningManager"
dataPath = "/Users/cfuta/Desktop/mlm-test-kit/framework/data/economies-of-scale.csv"
elements = {
    'create-button': element.get('Button', value='create')
    , 'name-field': element.get('TextField', value='name-entry')
    , 'next-button': element.get('Button', value='next')
    , 'type-option': element.get('Option', value='cluster')
    , 'algorithm-option': element.get('Option', value='dbscan')
    , 'csv-button': element.get('Button', value='csv')
    , 'load-data-button': element.get('Button', value='load-data')
    , 'file-upload': element.get('FileUpload')
    , 'confirm-create-button': element.get('Button', value='confirm-create')
}

driver = webdriver.get()
driver.get(url)
driver.implicitly_wait(1)

# Select Create Button
elements['create-button'].click(driver)

# Select Name Field and fill
elements['name-field'].fillText(driver)

# Select Next Button
elements['next-button'].click(driver)

# Select Type/Algorithm
elements['type-option'].click(driver)
elements['algorithm-option'].click(driver)

# Select Next Button
elements['next-button'].click(driver)

# Select Next Button
elements['next-button'].click(driver)

# Select CSV Button & upload file
elements['csv-button'].click(driver)
elements['file-upload'].upload(driver, dataPath)
elements['load-data-button'].click(driver)

# Select Next Button
elements['next-button'].click(driver)

# Select Save
elements['next-button'].click(driver)

# Confirm Create
elements['confirm-create-button'].click(driver)
