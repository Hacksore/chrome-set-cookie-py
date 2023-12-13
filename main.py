from fastapi import FastAPI
import chrome
import sqlite3
import constants

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
    # read sql lite file from the chrome dir
    sql_lite_file = f"{constants.chrome_tmp_path}/Default/Cookies"
    conn = sqlite3.connect(sql_lite_file)

    c = conn.cursor()
    c.execute('SELECT * FROM cookies')
    all_rows = c.fetchall()
    print(all_rows)

    return all_rows


@app.put("/cookie/:name")
def put_cookie():
    return []
