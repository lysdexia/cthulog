# TODO this shall be api
# TODO all endpoints protected
def starrywisdom(app, mongo):
    class Messages(object):
        def put(self, data):
            return True

        def get(self, args):
            posts = mongo.db.posts.find(args).sort([("stamp", -1)]).limit(100)
            return {
                    "section": args["section"],
                    "posts": posts
                    }

    return Messages()
