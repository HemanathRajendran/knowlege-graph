import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

URL = "https://www.tn.gov.in/scheme_list.php?dep_id=Mg=="

async def scrape():

    schemes = []

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        await page.goto(
            URL,
            wait_until="networkidle"
        )

        html = await page.content()

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        for link in soup.find_all("a"):

            text = link.get_text(strip=True)

            href = link.get("href")

            if text and href:

                if not href.startswith("http"):
                    href = (
                        "https://www.tn.gov.in/"
                        + href.lstrip("/")
                    )

                schemes.append(
                    {
                        "name": text,
                        "url": href
                    }
                )

        await browser.close()

    return schemes

if __name__ == "__main__":
    result = asyncio.run(scrape())
    print(result)