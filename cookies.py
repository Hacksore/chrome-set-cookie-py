import sqlite3
import constants

cookie_path = f'{constants.chrome_tmp_path}/Default/Cookies'


def fetch_all_cookies():

    db = sqlite3.connect(cookie_path)
    db.text_factory = lambda b: b.decode(errors="ignore")
    cursor = db.cursor()

    cursor.execute("""
    SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
    FROM cookies""")

    for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
        print(f"""
        Host: {host_key}
        Cookie name: {name}
        ===============================================================""")
    # close connection
    db.close()


def insert_cookie(name, value):
    db = sqlite3.connect(cookie_path)
    db.text_factory = lambda b: b.decode(errors="ignore")
    cursor = db.cursor()

    # insert cookie to chrome db
    cursor.execute("""
    INSERT INTO cookies (host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value, top_frame_site_key, path, is_secure, is_httponly, has_expires, is_persistent, priority, samesite, 'source_scheme', 'source_port', is_same_party, last_update_utc)
    VALUES ('127.0.0.1', ?, ?, 0, 0, 0, ?, '', '', false, true, true, true, true, 'lax', '', 8000, true, 0)""", (name, value, value))

    # commit changes
    db.commit()

    # close connection
    db.close()
