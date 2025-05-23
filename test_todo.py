#Page Object for To-Do Page
import pytest
from selenium import webdriver
from pages.todo_page import TodoPage
import allure

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://todomvc.com/examples/react/dist/")
    yield driver
    driver.quit()

@allure.feature("To-Do Application")
def test_todo_functionality(setup):
    page = TodoPage(setup)
    page.add_task("Task 1")
    page.add_task("Task 2")
    page.add_task("Task 3")

    page.mark_task_complete(1)
    page.delete_task(0)

    assert page.get_remaining_tasks() == ["Task 2", "Task 3"]
