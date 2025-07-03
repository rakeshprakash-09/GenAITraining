import asyncio
from playwright.async_api import async_playwright

async def save_amazon_phone_deals_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Go to Amazon India
        await page.goto("https://www.amazon.in")

        # Search for latest phone deals
        await page.fill("xpath=//*[@id='twotabsearchtextbox']", "latest phone deals")
        await page.press("xpath=//*[@id='twotabsearchtextbox']", "Enter")
        await page.wait_for_timeout(5000)  # Wait for search results to load

        # Save the entire search result page as HTML
        content = await page.content()
        with open("amazon_phone_deals.html", "w", encoding="utf-8") as f:
            f.write(content)

        print("Amazon phone deals page saved to amazon_phone_deals.html")

        await browser.close()

# Run the async function
asyncio.run(save_amazon_phone_deals_page())
