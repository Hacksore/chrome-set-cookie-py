from fastapi import FastAPI
import chrome
import cookies

app = FastAPI()

browser_handle = None


@app.on_event("startup")
async def startup_event():
    global browser_handle
    browser_handle = chrome.spawn_chrome_browser()
    print("Chrome process started", browser_handle.pid)


@app.on_event("shutdown")
async def shutdown_event():
    global browser_handle
    print("Shutting down")
    browser_handle.kill()


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.get("/cookies")
def get_cookies():
    return cookies.fetch_all_cookies()


@app.put("/cookie")
def put_cookie():
    return cookies.insert_cookie("test", "oke123")
