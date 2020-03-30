import json

import falcon


class StatusResource:

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'status': 'OK'})


app = falcon.API()


app.add_route('/v1/status', StatusResource())
