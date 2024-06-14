#JL Book Store#

This Selenium WebDriver automation project is written in python, and uses pytest framework. 
In order to run this project you need to install:
```
python
pytest
```


Project Structure: This project is build using Page Object Model and Data-Driven Tests. All files accessed by the Test Class is doing using Ralative Path for avoid dependencies with specific folder structure or particular Operating Systems.

Run Test suite: 
To run the entire Test suite just need to execute
```
pytest
```

for running test for a particular feature (e.g registation) you can  use
```
pytest -m registation
```

For running in verbose mode and see the details of execution
```
pytest -v
```

This suite is integrated with slack via slackhook, a configuration made on slack page. You can send your test results to slack using:
```
pytest -v --slack_hook = <Slack_hook_url>
```