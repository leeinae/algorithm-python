import datetime

FILTER_SIZE = 240 * 2 ** 10
FILTER_DATE = datetime.date(1990, 1, 31)
month_dic = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
             'Nov': 11, 'Dec': 12}


def solution(S):
    files = [s.strip().split(" ") for s in S.split("\n")]
    answer = []

    for file in files:
        size, day, month, year = int(file[0]), file[1], file[2], file[3]
        date = datetime.datetime.strptime(f'{year}-{month_dic[month]}-{day}', '%Y-%m-%d')
        if size >= FILTER_SIZE and date.date() > FILTER_DATE:
            answer.append(file)
    return str(len(answer))


solution(""" 779091968 23 Sep 2009 system.zip
 284164096 14 Aug 2013 to-do-list.xml
 714080256 19 Jun 2013 blockbuster.mpeg
       329 12 Dec 2010 notes.html
 444596224 17 Jan 1950 delete-this.zip
       641 24 May 1987 setup.png
    245760 16 Jul 2005 archive.zip
 839909376 31 Jan 1990 library.dll""")
