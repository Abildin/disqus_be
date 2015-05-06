from nose2.tools import such
# from sure import expect


with such.A("comment model") as it:

    @it.should("have a string representation")
    def test_comment_model():
        from core_app.models import Comment
        comment = Comment(title="abc", text="asdasd")
        comment_repr = str(comment)
        comment_repr.should.be.equal("abc: asdasd")
    it.createTests(globals())
