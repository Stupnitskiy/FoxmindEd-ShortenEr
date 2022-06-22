# FoxmindEd-ShortenEr
Simple link shortener as a test task for FoxmindEd

To run this app you should install it requirements.
To initiate db you should run basic migration comands:
```
flask db upgrade
```
It will create db instance with table for declared model.

There is a many things which I will never do from this code in production, I left one point in comment, at src.controller.upsert_link function. 
Keep in mind that I prefered to save my time instead of writing the best code. We can discuss anything much more deeper, if you want.

P.S. I was inspired by frontend in that article - https://www.freecodecamp.org/news/python-tutorial-how-to-create-a-url-shortener-using-flask/. 
