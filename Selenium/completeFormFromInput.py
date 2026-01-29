# Takes a users input and validates the responses. Once validates it will complete an online form with the answers provided by the user.


# import requirements

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

# use driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service) 


#Prompts user to input information for form
print("Enter your first name")
first_name = input()
print("Enter your last name")
last_name = input()
print("Enter your Job title")
job_title = input()


education_options = ["high school", "college", "grad school"]
while True:
    education = input("Enter your highest level of education: High School, College, Grad School").strip().lower()
    if education in education_options:
        print(f"Highest education: {education}" )
        break
    else:
        print("Invalid input, please choose again")


sex_options = ["male", "female", "prefer not to say"]
while True:
    sex = input("Enter your sex: Male, Female, Prefer not to say ").strip().lower()
    if sex in sex_options:
        print(f"sex: {sex}" )
        break
    else:
        print("Invalid input, please choose again")        



while True:
    date = input("Enter date in mm/dd/yyyy format: ")
    try:
        date_obj = datetime.strptime(date, "%m/%d/%Y")
        print(f"Valid date of: {date_obj.strftime("%B %d %Y")}")
        break
    except ValueError:
        print("Invalid format. Please enter date as mm/dd/yyyy")


print("Enter your years of experience in this field")
experience = int(input())






# Navigate to webpage and wait
driver.get("https://formy-project.herokuapp.com/form")
time.sleep(1)

# Finds first name field, empties and inputs first name
first_name_input = driver.find_element(By.ID, "first-name")
first_name_input.clear()
first_name_input.send_keys(first_name)

# Finds last name field, empties and inputs last name
last_name_input = driver.find_element(By.ID, "last-name")
last_name_input.clear()
last_name_input.send_keys(last_name)

# Finds Job title field, empties and inputs job title name
job_title_input = driver.find_element(By.ID, "job-title")
job_title_input.clear()
job_title_input.send_keys(job_title)

# Finds the Eduction radio button and selects it on previous input
match education:
    case "college":
        Education_radio_button_input = driver.find_element(By.ID, "radio-button-2")
        Education_radio_button_input.click()
    case "high school":
        Education_radio_button_input = driver.find_element(By.ID, "radio-button-1")
        Education_radio_button_input.click()
    case "grad school":
        Education_radio_button_input = driver.find_element(By.ID, "radio-button-3")
        Education_radio_button_input.click()
    case _:
        print ("Unknown input")

# Finds the Sex check box and selects it
match sex:
    case "male":
        Sex_checkbox_input = driver.find_element(By.ID, "checkbox-1")
        Sex_checkbox_input.click()
    case "female":
        Sex_checkbox_input = driver.find_element(By.ID, "checkbox-2")
        Sex_checkbox_input.click()
    case "prefer not to say":
        Sex_checkbox_input = driver.find_element(By.ID, "checkbox-3")
        Sex_checkbox_input.click()
    case _:
        print ("Unknown input")

# Finds the Years of Expierence option in drop down and selects it. Loops through each option until it finds correct one.
Experience_input = driver.find_elements(By.TAG_NAME, "option")
match experience:
    case 0 | 1:
        Experience_input[1].click()
    case 2 | 3 | 4:
        Experience_input[2].click()
    case 5 | 6 | 7 | 8 | 9:
        Experience_input[3].click()
    case 10 if experience >= 10:
        Experience_input[4].click()
    case _:
        print("No match")

#Finds the date input field and enters the date
Date_input = driver.find_element(By.ID, "datepicker")
Date_input.clear()
Date_input.send_keys(date)

time.sleep(3)

#Clicks submit button
Submit = driver.find_element(By.CLASS_NAME, "btn-lg")
Submit.click()

time.sleep(5)


# Quit google chrome
driver.quit()
