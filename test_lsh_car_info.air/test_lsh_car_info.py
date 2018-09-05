# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#exec_script("test_custom_info.air")
point1 = poco(text = "是否预约").get_position()
point2 = poco(text = "顾客姓名").get_position()
poco.swipe(point1,point2)
# point3 = poco(text = "接待备注").get_position()
# point4 = poco(text = "联系地址").get_position()
# poco.swipe(point3,point4)
try:
    is_sign=poco("com.iris.lshitaskse:id/tv_intention_1").get_text()
except Exception as e:
    is_sign = ''
if is_sign != "意向一":
    poco("com.iris.lshitaskse:id/tv_name_type").click()
    poco("com.iris.lshitaskse:id/tv_intention_car_model").click()
else:  poco("com.iris.lshitaskse:id/tv_intention_car_model").click()
    
point3 = poco("com.iris.lshitaskse:id/listview").child("android.widget.FrameLayout")[4].get_position()

#print('P1:',point4)
point4 = poco("com.iris.lshitaskse:id/listview").child("android.widget.FrameLayout")[1].get_position()
#print('p2:',point3)
#sleep(3)
#poco.swipe(point3,point4)
i=0
while i<10:
   try:
        touch(Template(r"tpl1536030049356.png", record_pos=(0.001, 0.596), resolution=(720, 1280)))

        #poco(text="CLA-CLASS").click()
        break
   except Exception  as e:
        poco.swipe(point3,point4)
        i+=1
        
        
touch(Template(r"tpl1536032977655.png", record_pos=(-0.036, 0.514), resolution=(720, 1280)))
touch(Template(r"tpl1536033005216.png", record_pos=(-0.037, 0.515), resolution=(720, 1280)))

poco("com.iris.lshitaskse:id/title").child("android.widget.TextView")[1].click()

poco.swipe([0.5, 0.9359375],[0.5, 0.365625])
#点击车辆信息挂车
poco("com.iris.lshitaskse:id/child3").child("com.iris.lshitaskse:id/ll_group").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("com.iris.lshitaskse:id/iv_arrow").click()
#poco("com.iris.lshitaskse:id/iv_arrow").click()
poco.swipe([0.5, 0.9359375],[0.5, 0.395625])
poco("com.iris.lshitaskse:id/rb_intent1").click()
is_yixiangdan = False
if is_yixiangdan == False:
    poco("com.iris.lshitaskse:id/tv_matchcar").click()
    sleep(20.0)
    try:
        poco("com.iris.lshitaskse:id/listview").child("android.widget.LinearLayout")[1].click()
        poco("com.iris.lshitaskse:id/tv_guache").click()

    except Exception as e:
        poco("com.iris.lshitaskse:id/title").child("android.widget.TextView")[0].click()
else:
    pass
    
poco.swipe([0.5, 0.9359375],[0.5, 0.365625])

