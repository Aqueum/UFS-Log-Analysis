#!/usr/bin/python3

import psycopg2


def get_pop_articles():
    """Return list of title-views tuples
    of 3 most popular articles by hits descending"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select articles.title, count(*) as num from articles, log "
              "where log.path like '%' || articles.slug "
              "group by articles.title "
              "order by num "
              "desc limit 3;")
    pop_articles = c.fetchall()
    db.close()
    return pop_articles


def get_pop_authors():
    """Return list of name-views tuples
    of most popular authors by hits descending"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select authors.name, count(*) as num "
              "from articles, authors, log "
              "where authors.id = articles.author "
              "and log.path like '%' || articles.slug "
              "group by authors.name "
              "order by num desc;")
    pop_authors = c.fetchall()
    db.close()
    return pop_authors


def get_bad_days():
    """Return list of date-%age tuples
    of dates when over 1% of requests gave errors"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("with percentages as "
              "(select log.time::timestamp::date as date, round( 100.0 * "
              "avg(case when status='404 NOT FOUND' then 1 else 0 end), 1) "
              "as percentage from log group by date) "
              "select * from percentages where percentage>=1 "
              "order by percentage desc;")
    bad_days = c.fetchall()
    db.close()
    return bad_days


def plain_text_out(question, data, parameter):
    """Take question string, list of tuples and parameter string
    print question & each list member on separate lines"""
    print("\n\n" + question + "\n")
    for line in data:
        print(str(line[0]) + " - " + str(line[1]) + parameter)


plain_text_out("1. What are the most popular three articles of all time?",
               get_pop_articles(), " views")
plain_text_out("2. Who are the most popular article authors of all time?",
               get_pop_authors(), " views")
plain_text_out("3. On which days did more than 1% of requests lead to errors?",
               get_bad_days(), "% errors\n\n\n")
