#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def doSwitch(locals, caseStr, args):

    def _sampleFunction(_args):
        pass
    funcType = type(_sampleFunction)  # to-do / FIXME: figure out how to specify this properly

    caseFuncs = {}
    for locName in locals.keys():
        if locName.startswith('case_') and type(locals[locName]) == funcType:
            caseName = locName[5:]
            caseFuncs[caseName] = locals[locName]

    # debug
    # print("caseFuncs: %s" % (caseFuncs,))
    # e.g.
    # caseFuncs: {
    # 'up': <function get_product.<locals>.case_up at 0x7f8b708f61f0>,
    # 'down': <function get_product.<locals>.case_down at 0x7f8b708f6280>,
    # 'forward': <function get_product.<locals>.case_forward at 0x7f8b708f6310>,
    # 'default': <function get_product.<locals>.case_default at 0x7f8b708f63a0>
    # }

    ret = None
    if caseStr not in caseFuncs:
       if 'default' in caseFuncs:
          ret = caseFuncs['default']
       else:
          print("WARNING: No default case defined, not running any case function for input case '%(caseStr)s'" % locals())
    else:
      # run our case!
      ret = caseFuncs[caseStr](args)

    return ret
