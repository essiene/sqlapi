import sqlapi


class News(sqlapi.Table):
    @sqlapi.columns
    def select_all(self):
        '''select * from news'''

    @sqlapi.columns
    def select_news_by_id(self,id):
        """select * from news where id = '%s'"""


class Comment(sqlapi.Table):

    @sqlapi.columns
    def select_all(self):
        '''select * from comment'''


def test_fetch():
    conn = sqlapi.connect("sqlite://foo:bar@localhost/sqlapi")

    news = News(conn)
    comment = Comment(conn)

    for n in news.select_news_by_id(1):
        print n.id, n.head, n.date_created, n.author
