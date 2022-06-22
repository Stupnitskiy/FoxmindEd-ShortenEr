from src import db
from src.models import Link
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
    short_id, views_amount = _get_shortened_link_info(original_url)
    if short_id:
        return short_id, views_amount

    while short_id is None:
        new_short_id = generate_random_string()
        link_info = Link.query.filter_by(short_id=new_short_id).first()
        if not link_info:
            short_id = new_short_id

    new_link = Link(original_url, short_id, 0)
    db.session.add(new_link)
    db.session.commit()

    return short_id, 0


def _get_shortened_link_info(original_url):
    link_info = Link.query.filter_by(original_url=original_url).first()
    if link_info:
        return link_info.short_id, link_info.views_amount

    return None, None


def process_redirect(short_id):
    link_info = Link.query.filter_by(short_id=short_id).first()

    if link_info:
        link_info.views_amount += 1
        db.session.commit()

        return link_info.original_url

    return None
