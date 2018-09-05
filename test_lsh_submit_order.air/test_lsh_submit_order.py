# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco(text="订单").click()
poco.swipe([0.5, 0.9359375],[0.5, 0.305525])
poco("com.iris.lshitaskse:id/tv_xiaosou_leixin").click()
#选择销售类型
poco(text="R1:正常零售").click()
#点击输入金额
poco("com.iris.lshitaskse:id/tv_input_jine").click()
#keyevent("Backspace")
text("15800")
poco("com.iris.lshitaskse:id/title").child("android.widget.TextView")[1].click()
#输入意向金无息退款天数
poco("com.iris.lshitaskse:id/tv_input_tuikuan_tianshu").click()
text("1")
poco("com.iris.lshitaskse:id/title").child("android.widget.TextView")[1].click()
#选择开票时间
poco("com.iris.lshitaskse:id/tv_input_yujikaipiaoriqi").click()
poco("com.iris.lshitaskse:id/btnSubmit").click()
poco("com.iris.lshitaskse:id/tv_tijiao").click()
poco("com.iris.lshitaskse:id/open").click()
sleep(3.0)
order_status = poco("com.iris.lshitaskse:id/tv_state").get_text()
assert_equal(order_status,"待审批","订单状态正确")
