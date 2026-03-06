# conftest.py
import os
import datetime
import pytest
import webbrowser

def pytest_configure(config):
    os.makedirs("htmlreports", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = f"htmlreports/report_{timestamp}.html"
    config._html_report_path = os.path.abspath(report_path)
    config.option.htmlpath = report_path
    config.option.self_contained_html = True

def pytest_unconfigure(config):
    report_path = getattr(config, "_html_report_path", None)
    if report_path and os.path.exists(report_path):
        webbrowser.open_new_tab(report_path)
