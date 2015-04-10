#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains Function that returns customer info, total orders, orders total"""


def sum_orders(customers, orders):
    """Process Customer orders, total and count of orders by customer.
    Args:
        customers (dict): Dictionary of Customers name and email.
        orders (dict): Dictionary of Orders containing total ammounts.
    Returns:
        results (dict): Dict. of total ammount of orders, and total order count.
    Examples:
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
                  3: {'customer_id': 2, 'total': 10},
                  4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                         3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'name': 'Person One',
             'email': 'email@one.com',
             'orders': 2,
             'total': 20}
         3: {'name': 'Person Two',
             'email': 'email@two.com',
             'orders': 1,
             'total': 15}}
    """
    results = {}
    for value in orders.itervalues():
        customerid = value['customer_id']
        total = value['total']
        if customerid in customers.keys():
            if customerid in results:
                results[customerid]['total'] += total
                results[customerid]['orders'] += 1
            else:
                results.update({customerid: {'total': total}})
                results[customerid].update({'orders': 0})
                results[customerid]['orders'] += 1
                results[customerid].update(customers[customerid])
    return results
