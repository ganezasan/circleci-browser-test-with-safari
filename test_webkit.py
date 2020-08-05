#coding: utf-8
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import time

def setUpModule():
    WebKitFeatureStatusTest.driver = webdriver.Safari()

def teardownModule():
    WebKitFeatureStatusTest.driver.quit()


class WebKitFeatureStatusTest(unittest.TestCase):
    
    def test_feature_status_page_search(self):
        self.driver.get("https://webkit.org/status/")
            
        # Enter "CSS" into the search box.
        # Ensures that at least one result appears in search
        search_box = self.driver.find_element_by_id("search")
        search_box.send_keys("CSS")
        value = search_box.get_attribute("value")
        self.assertTrue(len(value) > 0)
        search_box.submit()
        time.sleep(1)
        # Count the visible results when filters are applied
        # so one result shows up in at most one filter
        feature_count = self.shown_feature_count()
        self.assertTrue(feature_count > 0)
        
    def test_feature_status_page_filters(self):
        self.driver.get("https://webkit.org/status/")
            
        time.sleep(1)
        filters = self.driver.execute_script("return document.querySelectorAll('.filter-toggle')")
        self.assertTrue(len(filters) == 8)
    
    def shown_feature_count(self):
        return len(self.driver.execute_script("return document.querySelectorAll('li.feature:not(.is-hidden)')"))


if __name__ == "__main__":
    unittest.main()