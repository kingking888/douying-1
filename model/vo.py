from urllib import parse

class RequestVO():
    def __init__(self,info):
        self.info       = info
        self.scheme     = info['scheme']
        self.host       = info['host']
        self.method     = info['method'].lower()
        self.path       = info['path']
        self.headers    = info['headers']
        self.query      = info['query']
        self.form       = info.get('form')

        self.request_url = "%s://%s%s" % (self.scheme, self.host, self.path)

    def isGet(self):
        return self.method == "get"

    def get_query_str(self):
        query = self.query
        query_str = ''
        for k in query.keys():
            if query_str != '':
                query_str += "&"
            query_str += "%s=%s" % (k, query[k])

        return query_str

    def get_getmethod_url(self):
        return self.request_url + "?" + self.get_query_str()

    def get_url(self,*args,**kwargs):
        rst = None
        if self.method == 'get':
            if self.query.get('device_type'):
                self.query['device_type'] = self.query.get('device_type').replace(" ","%20")

            # query_str = parse.urlencode(self.query)
            url = self.get_getmethod_url()#parse.urlencode(self.query)
            rst = {'url': url, 'headers': self.headers}
        else:
            rst = {'url': self.request_url, 'query': self.form, 'headers': self.headers}

        return rst

class CommentListRequestVO(RequestVO):
    def __init__(self,info):
        super(CommentListRequestVO, self).__init__(info)

    # aweme_id,cursor
    def get_url(self,*args,**kwargs):
        if not kwargs['aweme_id']:
            raise Exception("aweme_id arg is not allowed null!")
        self.query['cursor']    = kwargs.get('cursor') or 0
        self.query['aweme_id']  = kwargs['aweme_id']
        return super(CommentListRequestVO,self).get_url(*args,**kwargs)


class SearchRequestVO(RequestVO):
    def __init__(self,info):
        super(SearchRequestVO, self).__init__(info)

    def get_url(self,*args,**kwargs):
        if self.isGet():
            if self.query:
                self.query['keyword'] = kwargs['keyword']
        elif self.form:
            self.form['keyword'] = kwargs['keyword']

        rst = super(SearchRequestVO,self).get_url(*args,**kwargs)
        rst['url'] = self.get_getmethod_url()


        return rst


# vo = CommentListRequestVO({
#     'scheme' :'https',
#     'host' : 'api3-normal-c-lq.amemv.com',
#     'method' : 'get',
#     'path' : '/aweme/v2/comment/list/',
#     'headers' : {},
#     'query' : {
#         'name':'smw',
#         'keyword':'减肥'
#     }
# })
#
# print(vo.get_url(aweme_id="d",cursor=2))