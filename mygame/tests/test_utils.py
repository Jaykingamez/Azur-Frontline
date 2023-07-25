"""
Tests of the utils module.

"""

from evennia.utils import create
from evennia.utils.test_resources import BaseEvenniaTest

from utils import utils
from objects import AzurObject


class TestUtils(BaseEvenniaTest):
    def test_get_obj_stats(self):

        obj = create.create_object(
            AzurObject, key="testobj", attributes=(("desc", "A test object"),)
        )
        result = utils.get_obj_stats(obj)

        self.assertEqual(
            result,
            """
|ctestobj|n
Value: ~|y0|n credits

A test object

Weight: |w1|n, Used from: |wbackpack|n
Quality: |wN/A|n, Uses: |wuses|n
Attacks using |wNo attack|n against |wNo defense|n
Damage roll: |wNone|n
""".strip(),
        )