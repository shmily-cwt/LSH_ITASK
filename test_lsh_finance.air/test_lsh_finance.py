# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco(text="金融").click()
actual_value=poco("com.iris.lshitaskse:id/tv_lable").get_text()
assert_equal(actual_value,"小计:￥100,237.41","金融检查成功")
poco(text="金融").click()
