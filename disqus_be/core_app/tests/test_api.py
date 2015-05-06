from nose2.tools import such
from sure import expect
from tastypie.test import TestApiClient
from attrdict import AttrDict
import json
import datetime


client = TestApiClient()


with such.A("comment API") as it:

    @it.should("allow to get list of all comments")
    def test_get_comments():
        resp = client.get("/api/v1/comment/")

        expect(resp.status_code).must.be.equal(200)
        data = json.loads(resp.content)
        data["meta"]["total_count"].should.be.equal(0)

    @it.should("allow to create a comment")
    def test_create_a_comment():
        url = "www.google.kz"
        resp = client.post("/api/v1/comment/", data={
            "title": "German",
            "email": "germanilyin@gmail.com",
            "text": "asdasd",
            "url": url
        })

        expect(resp.status_code).must.be.equal(201)

        data = AttrDict(json.loads(resp.content))
        data.title.should.be.equal("German")
        data.text.should.be.equal("asdasd")

        it.comment_uri = data.resource_uri

        data.url.should.be.equal(url)

    @it.should("allow to get number of comments by topic")
    def test_get_number_of_comments_by_topic():
        url = "www.google.kz"
        resp = client.get("/api/v1/comment/?url__iexact={}&total_count=true".format(url))

        expect(resp.status_code).must.be.equal(200)

        res = AttrDict(json.loads(resp.content))

        res.total_count.should.be.equal(1)

    @it.should("allow to get list of comments by topic")
    def test_get_comments_by_topic():
        url = "www.google.kz"
        resp = client.get("/api/v1/comment/?url__iexact={}".format(url))

        expect(resp.status_code).must.be.equal(200)

        res = AttrDict(json.loads(resp.content))
        res.meta.total_count.should.be.equal(1)

        res.objects[0].resource_uri.should.be.equal(it.comment_uri)

        'email'.should_not.be.within(res.objects[0])

    it.createTests(globals())
