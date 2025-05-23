from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TodoPage(BasePage):
    TODO_INPUT = (By.CLASS_NAME, "new-todo")
    CHECKBOXES = (By.CLASS_NAME, "toggle")
    DELETE_BUTTONS = (By.CLASS_NAME, "destroy")
    TODO_ITEMS = (By.CLASS_NAME, "todo")

    def add_task(self, task_name):
        input_box = self.find_element(self.TODO_INPUT)
        input_box.send_keys(task_name + "\n")

    def mark_task_complete(self, index):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        checkboxes[index].click()

    def delete_task(self, index):
        delete_buttons = self.driver.find_elements(*self.DELETE_BUTTONS)
        self.driver.execute_script("arguments[0].click();", delete_buttons[index])

    def get_remaining_tasks(self):
        return [item.text for item in self.driver.find_elements(*self.TODO_ITEMS)]
