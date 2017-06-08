# UFS-Log-Analysis
- Udacity Full Stack - Log Analysis project
- [Udacity Full Stack Web Developer Nanodegree](
https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) 
- Martin Currie (Aqueum) - 8 June 2017

# Getting Started
1. Ensure that you have functional copies of [Python 3](
https://www.python.org/downloads/), [PostgreSQL](
https://www.postgresql.org/download/) and [Psycopg2](
http://initd.org/psycopg/download/)
installed
2. [Download this repo](
https://github.com/Aqueum/UFS-Log-Analysis/archive/master.zip) 
to your own computer & unzip
3. [Download newsdata.sql](
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
from udacity and save it in the folder created in step 2
4. Open a unix command line (Terminal in macOS) navigate to the folder created
in step 2
5. Enter `psql -d news -f newsdata.sql` to load the database
6. Enter `python3 LogsAnalysis.py` to start a Log Analysis

# Known issues
## Date format
The date format deliberately doesn't match the example, I'm not American &
prefer the ISO standard that PostgreSQL defaults to.

## No views
In order to make the assessor's life easier, I decided not to use views. 
I don't like the idea of code that won't work out of the box
and don't think the queries were too tough to make without views anyway.

## Failed attempts not considered in popularity
While it may be considered that someone entering a URL that was intended to
reach an article was a vote for that article, it is assumed that any serious
attempt to view would end up with the correct URL.  Hence all 404 logs are 
ignored.

# Files
## newsdata.sql
NOT INCLUDED IN THIS REPO, see Getting Started step 3.

## LogsAnalysis.py
Source code python3 file.

## output.txt
Plain text example output
with input shell prompt & execution command.

# Contributing
This is an assessed project, so I'd probably get in trouble for accepting 
external input.

# Code Status
Can Udacity add a badge here..?

# License
GNU General Public License v3.0
See [LICENSE](https://github.com/Aqueum/UFS-Log-Analysis/blob/master/LICENSE)