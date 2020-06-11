import pytest
import unittest


def test_identify_unknown():
    import app
    import webtest
    app = main({})
    from webtest import TestApp
    testapp = TestApp(app)


def test_identify_known():
    from myproject import main
    app = main({})
    from webtest import TestApp
    .testapp = TestApp(app)


def test_record_new_user():
    res = self.testapp.get('/', status=200)
    self.assertTrue(b'Pyramid' in res.body)


if __name__ == '__main__':
    unittest.main()
