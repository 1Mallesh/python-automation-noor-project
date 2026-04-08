import os

def run(page, data, tc_id):
    url = "https://shankarbaba.org/contact-us/"

    try:
        page.goto(url)
        page.wait_for_selector("input[name='username']")

        page.fill("input[name='username']", data["name"])
        page.fill("input[name='mobile-number']", data["mobile"])
        page.fill("input[name='email']", data["email"])
        page.fill("input[name='address']", data["address"])
        page.fill("textarea[name='message']", data["message"])

        os.makedirs("screenshots", exist_ok=True)
        screenshot = "screenshots/shankara.png"
        page.screenshot(path=screenshot)

        return "PASS", screenshot, url

    except Exception as e:
        print("❌ Shankara ERROR:", e)
        return "FAIL", "", url