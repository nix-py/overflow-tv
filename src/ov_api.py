#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__    = "nix-py"
__date__      = "24-02-2017"
__license__   = "MIT"
__copyright__ = "Copyright © 2017 nix-py"


import requests
import collections


api_url = 'https://api.stackexchange.com/2.2'

def all_questions(tagname, order='asc', sort='activity'):
    """Get all the questions of specific tagname from stackoverflow.
    It provides following information about question
        * question tags
        * view count
        * answer count
        * link
        * quesition id
        * creation date
        * last acitivity date
        * title

    :tagname: str, name of tag
    :order: str, choose between `desc` or `asc`
    :sort: str, how you want to sort it, it accepts (activity, votes,
     creation, hot, week, month)
    :returns: generator, namedtuple
    """
    url = (
            api_url + 
            '/questions?'
            'order=order&'
            'sort=activity&'
            'tagged={tagname}&'
            'site=stackoverflow'.format(
                order=order, tagname=tagname, sort=sort,
                )
            )
    r = requests.get(url)
    json_data = r.json()
    data_tuple = collections.namedtuple(
            'data_tuple', [
                'tags', 'view_count', 'answer_count', 
                'link', 'question_id', 'creation_date',
                'last_activity_date', 'title',
                ]
            )
    for d in json_data['items']:
        yield data_tuple(
                tags=d['tags'], 
                view_count=d['view_count'],
                answer_count=d['answer_count'],
                link=d['link'],
                question_id=d['question_id'],
                creation_date=d['creation_date'],
                last_activity_date=d['last_activity_date'],
                title=d['title'],
                )
