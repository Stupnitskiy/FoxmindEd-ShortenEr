from src.utils.database import get_db_connection
from src.utils.random_string import generate_random_string


def upsert_link(original_url):
    """
    For me the best solution is to delegate this work to database.
    I mean to create a function which will generate short_id and check if it's not used yet.
    It's possible with relational DB functions written on procedure language.
    But I want to save my time and use SQLite, which has no support of procedure language.

    :param original_url: string
    :return: string, int
    """
    connection = get_db_connection()

    short_id, views_amount = _get_shortened_link_info(original_url, connection)
    if short_id:
        return short_id, views_amount

    while short_id is None:
        new_short_id = generate_random_string()
        search_query = """
            select * from links 
            where short_id=?
            limit 1;
        """
        res = connection.execute(search_query, (new_short_id,)).fetchone()
        if not res:
            short_id = new_short_id

    insert_query = 'insert into links (original_url, short_id, views_amount) values (?, ?, 0)'
    connection.execute(insert_query, (original_url, short_id))
    connection.commit()
    connection.close()

    return short_id, 0


def _get_shortened_link_info(original_url, connection):
    search_query = """
        select short_id, views_amount from links 
        where original_url=?
        limit 1;
    """
    res = connection.execute(search_query, (original_url,)).fetchone()
    if res:
        return res["short_id"], res["views_amount"]

    return None, None


def process_redirect(short_id):
    connection = get_db_connection()

    search_query = """
        select original_url from links 
        where short_id=?
        limit 1;
    """
    res = connection.execute(search_query, (short_id,)).fetchone()
    if res:
        increment_query = """
            update links set views_amount = views_amount + 1
            where short_id=?
        """
        connection.execute(increment_query, (short_id,))
        connection.commit()
        connection.close()

        return res["original_url"]

    return None
