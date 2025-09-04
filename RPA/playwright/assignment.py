import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  
        page = await browser.new_page()
        await page.goto("https://www.bing.com")

        #Find search box using your XPath
        search_box = await page.wait_for_selector('xpath=//*[@id="sb_form_q"]')
        await page.wait_for_timeout(2000)
        await search_box.fill("Gen AI update latest news")
        await search_box.press("Enter")
        await page.wait_for_timeout(5000)

        check_box = await page.wait_for_selector('xpath=//*[@id="LsMgo8"]/div/label/input')
        await check_box.check()
        await page.wait_for_timeout(2000)

    '''    text = await page.inner_text("body")
        with open("bing_page.txt", "w", encoding="utf-8") as f:
            f.write(text)

        await browser.close()
        print("✅ Saved page text -> bing_page.txt")'''


if __name__ == "__main__":
    asyncio.run(main())
