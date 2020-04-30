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

        self.search_url = None

    def isGet(self):
        return self.method == "get"

    def _generate_search_url(self):
        query = self.query
        query_str = ''
        for k in query.keys():
            if query_str != '':
                query_str += "&"
            if k == 'keyword':
                query_str += "keyword=%s"
            else:
                query_str += "%s=%s" % (k, query[k])


        self.search_url = "%s://%s%s" % (self.scheme, self.host, self.path)
        return self.search_url

    def get_search_url(self,word):
        if self.search_url == None:
            self._generate_search_url()

        self.query['keyword'] = word


        rst = None

        if self.method == 'get':
            query_str = parse.urlencode(self.query)
            url = self.search_url + "?" + query_str
            rst = {'url':url,'headers':self.headers}
        else:
            rst = {'url':self.search_url,'query':self.query,'headers':self.headers}

        return rst


# vo = RequestVO({
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
# print(vo.get_search_url('减肥'))