# circleci-browser-test-with-safari

This is example project for test with safari browser.
The project has circleci config and it has two tests. One uses webdriver and another uses standalone selenium server.

Python program is based on the below article.
> https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari

## Enable webdriver support

On CI environment, just `safaridriver --enable` command doesn't enable the webdriver support, it needs to do steps below.

```
defaults write com.apple.Safari IncludeDevelopMenu YES
defaults write com.apple.Safari AllowRemoteAutomation 1
sudo safaridriver --enable
safaridriver -p 0 &
```

