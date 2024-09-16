from playwright.async_api import async_playwright
import asyncio
import time
import re


# List of tuples to match company workday and its corresponding passwords
websites_list = [
    ('#Workday Website', '#Password'),
    ('#Workday Website', '#Password'),
]

websites = [x[0] for x in websites_list]


async def main(i):
    async with async_playwright() as playwright:

        browser = await playwright.firefox.launch(headless=False, slow_mo=50)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(websites_list[i][0])

        await page.click('text=Sign In')

        await page.fill('input[data-automation-id="email"]', '#Email') #Input email 
        await page.fill('input[data-automation-id="password"]', websites_list[i][1])

        time.sleep(1)

        await page.locator('[data-automation-id="click_filter"]').click()

        await page.click('text=Candidate Home')

        time.sleep(10)

        await browser.close()

if __name__ == '__main__':
    for sites in range(0, len(websites_list)):
        print(websites[sites])
        asyncio.run(main(sites))
