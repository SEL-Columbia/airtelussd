import unittest
from pyramid.httpexceptions import HTTPMethodNotAllowed
from pyramid import testing


class ViewTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_view_not_allowed(self):
        from airtelussd import index_menu
        request = testing.DummyRequest()
        resp = index_menu(request)
        self.assertTrue(isinstance(resp, HTTPMethodNotAllowed))
