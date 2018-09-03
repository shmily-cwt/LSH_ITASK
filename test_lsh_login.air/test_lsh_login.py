# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
start_app("com.iris.lshitaskse")
sleep(5)
txt =  ''
try:
    txt = poco(text="登 录").get_text()  
    print(u'txt:',txt)
except BaseException as e:
    txt = ''
    print (u'未获取到元素:',e)
	
sleep(5)
    
if txt == '登 录':
    poco("com.iris.lshitaskse:id/et_login_user").click()
    text("cwt@lsh.com")
    poco("com.iris.lshitaskse:id/et_login_psw").click()
    text('111111')
    #keyevent('Enter')
    poco("com.iris.lshitaskse:id/btn_login").click()
    expect_value = "时间"
    actual_value = poco(text="时间").get_text()
    assert_equal(actual_value, expect_value, "验证登录成功！")

else:
    poco("com.iris.lshitaskse:id/im_circle").click()
    poco(text="退出登录").click() 
    poco("com.iris.lshitaskse:id/et_login_user").click()
    text("cwt@lsh.com")
    poco("com.iris.lshitaskse:id/et_login_psw").set_text('111111')
    #text("111111")
    keyevent('Enter')
    poco("com.iris.lshitaskse:id/btn_login").click()
    expect_value = "时间"
    actual_value = poco(text="时间").get_text()
    assert_equal(actual_value, expect_value, "验证登录成功！")