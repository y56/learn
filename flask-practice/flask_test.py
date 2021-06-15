#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

HTTP toy service in Flask

1.

/echo: GET; only support GET, a 405 if other than GET

    * payload:
        text: my_text

    * Only `text` is allowed, no `text` or other than `text` leads a 406.

    * If everything looks good, echo the text.

2.

/set_title: POST; only support POST, a 405 if other than POST

    * payload:
        title: my_title

    * Only `title` is allowed, no `title` or other than `title` leads a 406.

    * head `password` as 5566, otherwise return a 403

    * If everything looks good, return an empty response.

    * After a correct POST, later `/echo` responses should all have header
      `title: my_title`.

TODO:

    * Do all sessions/connections/processes/threads share the same `title`?
      Will one user's `echo()` be affected by another user's `set_title()`

    * If the parameter (ie, `title`) is shared to some extend,
      should `set_title()` block `echo()`?

    * How to write unit test?

"""

from flask import Flask, request, Response

my_title = None

app = Flask(__name__)

@app.route("/echo", methods=["GET"])
def echo():
    text = request.args.get("text")
    all_paras = request.args

    if text and len(all_paras) == 1:
        resp = Response(text)
        if my_title:
            resp.headers["title"] = my_title
        return resp

    status_code = Response(status=406)
    return status_code

@app.route("/set_title", methods=["POST"])
def set_text():
    password = request.headers.get("password")
    if password or password != "5566":
        status_code = Response(status=403)
        return status_code

    data = request.get_json()
    global my_title  # TODO: a better way to pass parameters between endpoints
    my_title = data["title"]

    return ('', 204)


if __name__ == "__main__":
    app.run()
