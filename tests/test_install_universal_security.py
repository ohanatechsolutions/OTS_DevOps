"""Offline tests for the cross-repository security onboarding tool."""
import contextlib
import io
import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.abspath("scripts"))
import install_universal_security as install


class OnboardingTests(unittest.TestCase):
    def run_main(self, target, response):
        def api(method, endpoint, payload=None, allow_404=False):
            response.append((method, endpoint, payload))
            if endpoint.endswith("/contents/" + install.PATH + "?ref=main"):
                return None
            if endpoint.endswith("/git/ref/heads/main"):
                return {"object": {"sha": "a" * 40}}
            if endpoint.endswith("/pulls"):
                return {"html_url": "https://github.com/ohanatechsolutions/Example/pull/1"}
            return {"default_branch": "main", "archived": False, "disabled": False, "fork": False}
        with mock.patch.dict(os.environ, {"GH_TOKEN": "fake-token"}):
            with mock.patch.object(sys, "argv", ["installer", "--repository", target]):
                with mock.patch.object(install, "gh", side_effect=api):
                    with contextlib.redirect_stdout(io.StringIO()):
                        return install.main()

    def test_generates_pull_request_not_direct_main_commit(self):
        calls = []
        self.assertEqual(self.run_main("ohanatechsolutions/Example", calls), 0)
        self.assertEqual([method for method, _, _ in calls],
                         ["GET", "GET", "GET", "POST", "PUT", "POST"])
        self.assertIn("security-onboarding", calls[4][2]["branch"])
        self.assertEqual(calls[-1][2]["base"], "main")
        self.assertEqual(calls[-1][2]["head"], calls[4][2]["branch"])

    def test_rejects_cross_owner(self):
        with mock.patch.dict(os.environ, {"GH_TOKEN": "fake-token"}):
            with mock.patch.object(sys, "argv", ["installer", "--repository", "someoneelse/Example"]):
                with self.assertRaises(SystemExit):
                    install.main()

    def test_template_is_pinned_and_read_only(self):
        content = install.caller()
        self.assertIn("@" + install.BASELINE, content)
        self.assertIn("contents: read", content)
        self.assertNotIn("contents: write", content)


if __name__ == "__main__":
    unittest.main()
