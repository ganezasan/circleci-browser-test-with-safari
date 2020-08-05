const { Builder, By } = require("selenium-webdriver");

async function main() {
  const driver = new Builder()
  .forBrowser("safari")
  .usingServer('http://localhost:4444/wd/hub')
  .build();

  await driver.get("https://webkit.org/status/");

  driver.quit();
}

main();