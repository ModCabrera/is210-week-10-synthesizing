#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import unittest


# Import user libs
import data
import task_01


class Task01TestCase(unittest.TestCase):
    """Task 01 tests"""

    answer = {1: {'email': 'evorsoisson@komarr.net',
                  'name': 'Ekaterin Vorsoisson',
                  'orders': 3,
                  'total': 1287},
              2: {'email': 'cordelia@beta.com',
                  'name': 'Cordelia Naismith',
                  'orders': 5,
                  'total': 2778},
              3: {'email': 'iv398@barrayar.net',
                  'name': 'Ivan Vorpatril',
                  'orders': 3,
                  'total': 358},
              4: {'email': 'viceroy@sergyar.net',
                  'name': 'Aral Vorkosigan',
                  'orders': 5,
                  'total': 1207},
              5: {'email': 'admiral@dendarii.com',
                  'name': 'Eli Quinn',
                  'orders': 3,
                  'total': 451},
              6: {'email': 'portmaster@graf.net',
                  'name': 'Bel Thorne',
                  'orders': 3,
                  'total': 1198},
              7: {'email': 'impsec@barrayar.net',
                  'name': 'Simon Illyan',
                  'orders': 3,
                  'total': 1897},
              8: {'email': 'dg1367@barrayar.net',
                  'name': 'Duv Galeni',
                  'orders': 1,
                  'total': 204},
              9: {'email': 'impsec@barrayar.net',
                  'name': 'Gregor Vorbarra',
                  'orders': 2,
                  'total': 1704}}

    def test_sum_orders(self):
        """Tests the value of the NIGEL constant."""
        returned = task_01.sum_orders(data.CUSTOMERS, data.ORDERS)
        self.assertEqual(returned, self.answer)


if __name__ == '__main__':
    unittest.main()
