from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import pytest


class TodoAutomation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://todomvc.com/examples/react/dist/")

    def test_todo_operations(self):
        driver = self.driver

        # Add three tasks
        tasks = ["Task 1", "Task 2", "Task 3"]
        input_box = driver.find_element(By.CLASS_NAME, "new-todo")

        for task in tasks:
            input_box.send_keys(task)
            input_box.send_keys(Keys.RETURN)

        # Mark second task as complete
        checkboxes = driver.find_elements(By.CLASS_NAME, "toggle")
        checkboxes[1].click()

        # Delete first task
        delete_buttons = driver.find_elements(By.CLASS_NAME, "destroy")
        driver.execute_script("arguments[0].click();", delete_buttons[0])

        # Validate UI status
        todo_items = driver.find_elements(By.CLASS_NAME, "todo")
        remaining_tasks = [item.text for item in todo_items]

        self.assertEqual(remaining_tasks, ["Task 2", "Task 3"])  # "Task 1" should be deleted

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
