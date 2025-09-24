from playwright.sync_api import Page
import pytest

#@pytest.mark.skip_browser("firefox")


#pytest.mark.only_browser("firefox")

def test_title(page :Page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs1"

def test_inventory(page :Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."