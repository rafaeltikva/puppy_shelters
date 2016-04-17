__author__ = 'rafaeltikva'

import datetime

def current_time():
    return datetime.datetime.utcnow()


def date_from_days_ago(days_ago):
    return current_time() - datetime.timedelta(days_ago)



