#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just some docstring"""
import pprint

CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
             3: {'name': 'Person Two', 'email': 'email@two.com'}
             }
ORDERS = {1: {'customer_id': 2, 'total': 10},
          3: {'customer_id': 2, 'total': 10},
          4: {'customer_id': 3, 'total': 15}
          }


def sum_orders(customers, orders):
    new_dict = customers.copy()
    for customerkey, customerinfo in customers.iteritems():
        customerinfo.update({'orders': 0, 'total':0})
        for field1, value1 in orders.iteritems():
           if customerkey == value1['customer_id']:
               customerinfo['total'] += value1['total']
               customerinfo['orders'] += 1
    return new_dict

            
if __name__ == '__main__':
    pprint.pprint(sum_orders(CUSTOMERS, ORDERS))
