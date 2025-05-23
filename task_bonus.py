import { Builder, By, Key, until, WebDriver } from "selenium-webdriver";

(async function todoTest() {
    let driver: WebDriver = await new Builder().forBrowser("chrome").build();
    try {
        await driver.get("https://todomvc.com/examples/react/dist/");

        let inputBox = await driver.findElement(By.className("new-todo"));

        // Add three tasks
        const tasks = ["Task 1", "Task 2", "Task 3"];
        for (let task of tasks) {
            await inputBox.sendKeys(task, Key.RETURN);
        }

        // Mark second task as complete
        let checkboxes = await driver.findElements(By.className("toggle"));
        await checkboxes[1].click();

        // Delete first task
        let deleteButtons = await driver.findElements(By.className("destroy"));
        await driver.executeScript("arguments[0].click();", deleteButtons[0]);

        // Validate UI status
        let todoItems = await driver.findElements(By.className("todo"));
        let remainingTasks = [];
        for (let item of todoItems) {
            remainingTasks.push(await item.getText());
        }

        console.log("Remaining tasks:", remainingTasks);
    } finally {
        await driver.quit();
    }
})();
