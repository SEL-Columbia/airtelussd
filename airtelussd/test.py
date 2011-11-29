import unittest
from pyramid.response import Response
from pyramid.httpexceptions import (
    HTTPMethodNotAllowed,
    HTTPClientError)
from pyramid import testing


class ViewTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_view_not_allowed(self):
        """
        We don't allow get requests
        """
        from airtelussd import index
        request = testing.DummyRequest()
        resp = index(request)
        self.assertTrue(isinstance(resp, HTTPMethodNotAllowed))

    def test_post_request(self):
        """
        Test the post request, with empty post data
        """
        from airtelussd import index
        request = testing.DummyRequest(post={})
        self.assertRaises(HTTPClientError, index, request)

    def test_post_requires(self):
        """
        Test the index view function with the correct data.
        """
        from airtelussd import index
        request = testing.DummyRequest(
            post={'REQUESTNEW': True,
                  'INPUT': '',
                  'SESSIONID': '123455'})
        resp = index(request)
        self.assertTrue(isinstance(resp, Response))
