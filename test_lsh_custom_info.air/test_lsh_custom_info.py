# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#print(hunter)
#print("add:",add)
#exec_script("test_login.air")

mobile = '15533308760'
custom_name = '自动化1'
email = '877180064@qq.com'



#print("这是我的：",common.a)


poco("com.iris.lshitaskse:id/fragment_btm_bt").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[2].child("android.widget.TextView").click()
poco(text="接待完善").click()
txt = poco("com.iris.lshitaskse:id/tv_cus_name").get_text()
print(txt)
if txt != '新进店':
    print("未推送新进店客户，请查看测试报告")
else:
    poco("com.iris.lshitaskse:id/listview").child("android.widget.FrameLayout")[0].child("com.iris.lshitaskse:id/ll_item_bg").child("android.widget.RelativeLayout").child("com.iris.lshitaskse:id/ll_cus_info").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("com.iris.lshitaskse:id/tv_cus_name").click()
    poco("com.iris.lshitaskse:id/rb_sex_female").click()
    poco("com.iris.lshitaskse:id/tv_cus_phone").click()
    #text("15533340987")
    poco("com.iris.lshitaskse:id/et_mail_content").click()
    text("15533395673")
    poco("com.iris.lshitaskse:id/title").child("android.widget.TextView")[1].click()
    poco("com.iris.lshitaskse:id/tv_cus_name").click()
    text('abcd')
    poco("com.iris.lshitaskse:id/title").child("android.widget.TextView")[1].click()
    poco("com.iris.lshitaskse:id/tv_email").click()
    text('877181064@qq.com')
    poco("com.iris.lshitaskse:id/title").child("android.widget.TextView")[1].click()

    poco("com.iris.lshitaskse:id/tv_id_card").click()
    text('123444133440987365')
    poco("com.iris.lshitaskse:id/title").child("android.widget.TextView")[1].click()
    poco("com.iris.lshitaskse:id/tv_province").click()
    poco(text="北京市").click()
    poco("com.iris.lshitaskse:id/tv_city").click()
    poco("com.iris.lshitaskse:id/tv_name").click()
    poco("com.iris.lshitaskse:id/tv_canton").click()
    poco(text="东城区").click()
    poco("com.iris.lshitaskse:id/tv_address").click()
    text("是大家都会胜多负少")
    poco("com.iris.lshitaskse:id/title").child("android.widget.TextView")[1].click()
    poco("com.iris.lshitaskse:id/tv_intention_level").click()
    poco(text="A:一周内订单").click()