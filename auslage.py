class GuestbookHandler(Basehandler):
    def get(self):
        entry = Guestbook.query().fetch()
        params = {}
        params["entries"] = entry
        return self.render_template("gaestebuch.html", params

def post(self):
    params = {}
    name = self.request.get("name")
    if name == None:
        name = "Anonymous"
    email = self.request.get("email")
    comment = self.request.get("comment")
    params.update({"name": name, "email": email, "comment": comment})
    entry = Guestbook(name=params["name"], email=params["email"], text=params["comment"])
    entry.put()
    return self.render_template("comment.html", params)