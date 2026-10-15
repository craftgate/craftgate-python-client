import os
import unittest

import craftgate
from craftgate import RequestOptions
from craftgate._version import VERSION
from craftgate.adapter.base_adapter import BaseAdapter


class ClientVersionTest(unittest.TestCase):

    def test_version_module_is_part_of_the_package(self):
        version_file = os.path.join(os.path.dirname(craftgate.__file__), "_version.py")
        self.assertTrue(os.path.isfile(version_file))

    def test_should_send_client_version_header(self):
        adapter = BaseAdapter(RequestOptions(api_key="api-key", secret_key="secret-key",
                                             base_url="https://sandbox-api.craftgate.io"))

        headers = adapter._create_headers(None, "/payment/v1/card-payments")

        self.assertEqual("craftgate-python-client:" + VERSION, headers["x-client-version"])


if __name__ == "__main__":
    unittest.main()
