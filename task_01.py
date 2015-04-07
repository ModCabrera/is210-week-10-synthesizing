#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just some docstring"""

def sum_orders(customers, orders):
    new_dict = customers.copy()
    for customerkey, customerinfo in customers.iteritems():
        customerinfo.update({'orders': 0, 'total': 0})
        for field1, value1 in orders.iteritems():
            if customerkey == value1['customer_id']:
                customerinfo['total'] += value1.get('total')
                customerinfo['orders'] += 1
    return new_dict
