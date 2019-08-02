# one-day-webcrawler
Created using python module scrapy

a webcrawler that crawls the frontend of the website to obtain html data.

To use python virtual environment
1. `pip install virtualenv`
2. cd to your virtual environment directory
3. `virtualenv env`
4. `\env\Scripts\activate.bat`
5. Place project folder into virtual environment directory


```
pip install scrapy
pip install pypiwin32
```

How to use crawler (Ensure that pwd is in project directory with scrapy.cfg)

`scrapy crawl spooders -o data.json`

or

`scrapy runspider jokeSpider.py -o data.json`
