# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco(text="保险").click()
actual_value=poco("com.iris.lshitaskse:id/child5").child("com.iris.lshitaskse:id/ll_group").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("com.iris.lshitaskse:id/tv_lable").get_text()

#actual_value = poco("com.iris.lshitaskse:id/tv_lable").get_text()
assert_equal(actual_value,"(交强险+商业险)小计:11,820.26","保险验证成功")
poco(text="保险").click()
