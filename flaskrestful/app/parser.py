#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from parsed_data.models import BlogData
import os
import django
# BlogData를 import해옵니다
from parsed_data.models import BlogData



class Parser:
    def __init__(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
        django.setup()

    def parse_blog(self):
        for i in range(4300,4752,1):
            req = requests.get('https://www.campuspick.com/activity/view?id='+str(i))
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            my_titles = soup.select(
                'h1'
            )
            my_image = soup.select(
                '.poster > img'
            )
            my_explanation = soup.select(
                'article.description'
            )
            my_company = soup.select(
                'p.company'
            )
            my_dday = soup.select(
                '.dday + p.indent'
            )
            
            if len(my_explanation) == 0 :
                continue
            for title in my_titles:
                activity_title = str(title)
            for image in my_image:
                activity_image = image.get('href')
            for explanation in my_explanation:
                activity_explanation = str(explanation)
            for company in my_company:
                activity_company = str(company)
            for d_day in my_dday:
                activity_d_day = str(d_day)
                
            BlogData(title = activity_title, image = activity_image, explanation = activity_explanation, company = activity_company, d_day = activity_d_day).save()
