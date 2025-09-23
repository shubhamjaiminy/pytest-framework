from playwright.async_api import async_playwright
import asyncio

async def main():
   async  with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.cityexperiences.com/")
        await page.screenshot(path="example.png")
        print(await page.title())
    

asyncio.run(main())