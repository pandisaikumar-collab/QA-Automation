import os 
import time 
import pytest 
import logging 

log = logging.getLogger(os.path.dirname(__file__))
log.setLevel(logging.INFO)


def test_demo_home_page(driver, config, home_obj, elements_obj, progress_bar):
    if home_obj.is_demoqa_page_loaded():
        home_obj.click_elements_button()
        if elements_obj.is_elements_page_loaded():
            home_obj.click_widgets_section()
            #assert progress_bar.click_widgets_section()
        # if elements_obj.is_widgets_page_loaded():
        #     assert True, "Widgets page loaded successfully"
        #     elements_obj.click_progress_bar_section()
            # table_data = elements_obj.get_web_table_data()
            # if table_data:
            #     log.info(f"Table data: %s", table_data)
            # else:
            #     pytest.fail("No data found in the web table")
    else:
        pytest.fail("Failed to load Demo Home page")


def test_progress_bar(driver, config, progress_bar):
    #progress_bar.is_widgets_page_loaded()
    progress_bar.click_progress_bar_section()
    time.sleep(5)
    progress_bar.handle_progress_bar()
    time.sleep(5)
    
    


