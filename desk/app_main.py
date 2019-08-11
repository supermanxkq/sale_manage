# -*- coding: utf-8 -*-

from django import template

register = template.Library()


# 仿百度分页
@register.filter(is_safe=True)
def paging(value, index):
    if value <= 10:
        if index < 6:
            return range(1, value + 1)
        return range(1, value + 1)
    if value > 10:
        if value % 10 == 0:
            if index <= 6:
                return range(1, 11)
            if index > 6:
                return range(index - 5, index + 5)
        if value % 10 != 0:
            if index <= 6:
                return range(1, 11)
            if value - index > 4:
                return range(index - 5, index + 5)
            if value - index <= 4:
                return range(value - 9, value + 1)


