import urllib3

class HttpClient:
	__baseurl = ''

	def __init__(self, baseurl):
		self.http = urllib3.PoolManager()
		self.__baseurl = baseurl

	def set_baseurl(self, baseurl):
		self.__baseurl = baseurl
		return self

	def get(self, path, headers = {}):
		url = self.__baseurl + path
		response = self.http.request("GET", url, headers=headers)
		return response.data.decode('ISO-8859-1')