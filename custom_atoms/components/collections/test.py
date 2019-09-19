# -*- coding: utf-8 -*-

from pipeline.conf import settings
from pipeline.core.flow.activity import Service
from pipeline.component_framework.component import Component

__group_name__ = u"自定义原子(TEST2)"

class TestSimpleService(Service):
    __need_schedule__ = False

    def execute(self, data, parent_data):
        print(data, parent_data)
        test_radio = data.get_one_of_inputs('test_radio')
        test_textarea = data.get_one_of_inputs('test_textarea')
        test_input = data.get_one_of_inputs('test_input')

        print(test_radio,test_textarea,test_input)
        if int(test_input) + int(test_textarea) + int(test_radio) >= 10:
            return True
        else:
            data.set_outputs('ex_data', u"参数和小于10,请重新填参")
            return False

    def outputs_format(self):
        return []

    # def outputs_format(self):
    #     return [
    #         self.OutputItem(name=_(u'结果数据1'), key='data1', type='string')
    #     ]

class TestSimpleComponent(Component):
    name = u'简单原子2'
    code = 'test_simple'
    bound_service = TestSimpleService
    form = settings.STATIC_URL + 'custom_atoms/test/test_simple.js'