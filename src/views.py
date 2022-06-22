from src import app

from flask import render_template, request, redirect, flash, url_for
from flask.views import MethodView

from src.controller import upsert_link, process_redirect


class IndexView(MethodView):
    @staticmethod
    def get():
        return render_template('index.html')

    @staticmethod
    def post():
        url = request.form.get('url')

        if not url:
            flash('The URL is required!')
            return redirect(url_for('index_view'))

        short_id, views_amount = upsert_link(url)

        return render_template('index.html', short_url=short_id, views_amount=views_amount)


@app.route('/<short_id>')
def redirect_url(short_id):
    original_url = process_redirect(short_id)
    if original_url:
        return redirect(original_url)
    else:
        flash('Invalid URL')
        return redirect(url_for('index_view'))


index_view = IndexView.as_view('index_view')
app.add_url_rule('/', view_func=index_view, methods=['GET'])
app.add_url_rule('/', view_func=index_view, methods=['POST'])
