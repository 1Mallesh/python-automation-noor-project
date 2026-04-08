import os

def run(page, data, tc_id):   # ✅ colon added
    try:
        url = "https://saburi.works/contact/"
        page.goto(url)

        page.wait_for_selector("input[name='fname']")

        page.fill("input[name='fname']", data["name"])
        page.fill("input[name='email']", data["email"])
        page.fill("input[name='phonenumber']", data["phone"])
        page.fill("input[name='companyname']", data["company"])

        page.select_option("select[name='city']", data["city"])
        page.select_option("select[name='lookingFor']", data["service"])

        page.fill("textarea[name='message']", data["message"])

        os.makedirs("screenshots", exist_ok=True)
        screenshot = f"screenshots/{tc_id}_saburi.png"
        page.screenshot(path=screenshot)

        return "PASS", screenshot, url

    except Exception as e:
        print("❌ Saburi ERROR:", e)
        return "FAIL", "", url