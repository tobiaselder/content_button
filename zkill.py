import requests

_urlbase = 'https://zkillboard.com/api/'
_headers = {
      'accept-encoding': 'gzip',
      'user-agent': 'content_button/0.1',
      'maintainer': 'pieflinger@gmail.com'
   }

def get_kills(sys_ids, timespan=900):
   ids = ','.join(sys_ids)
   url = _urlbase + "systemID/{}/".format(ids)
   if timespan is not None:
      url += "pastSeconds/{}/".format(timespan)
   r = requests.get(url, headers=_headers)

   return r.json()

   #30003942,30003943




