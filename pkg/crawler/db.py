import psycopg2

def insert_query(driver):
    
    conn = psycopg2.connect(
    host="localhost",
    database="insta",
    user="postgres",
    password="password")

    cursor = conn.cursor()

    scraped_data_table_insert_query = """ INSERT INTO scraped_data (user_id, name, followers, following, post_number, total_comment, total_likes) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    followers_insert_query = """ INSERT INTO followers (user_id, follower_account) VALUES (%s,%s) """
    followings_insert_query = """ INSERT INTO followings (user_id, following_account) VALUES (%s,%s) """

    record_for_scraped = ("1", username, follower, following, post, comments, likes)

    cursor.execute(scraped_data_table_insert_query, record_for_scraped)
    conn.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into scraped_data table")


    for f in followers:
        d = ["1", f]
        cursor.execute(followers_insert_query, d)
        conn.commit()
        count = cursor.rowcount

    print(count, "Record inserted successfully into scraped_data table")

    for f in followings:
        d = ["1", f]
        cursor.execute(followings_insert_query, d)
        conn.commit()
        count = cursor.rowcount

    print(count, "Record inserted successfully into scraped_data table")
    return
