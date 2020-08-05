const { Builder, By } = require("selenium-webdriver");

async function main() {
  const driver = new Builder()
  .forBrowser("safari")
  .usingServer('http://localhost:4444/wd/hub')
  .build();

  try {
    await driver.get("https://webkit.org/status/");
    const title = await (await driver.findElement(By.id('logo'))).getText();
    console.log(title);
  } catch (e) {
    driver.quit();
    throw new Error(e);
  }
  driver.quit();
}

main();