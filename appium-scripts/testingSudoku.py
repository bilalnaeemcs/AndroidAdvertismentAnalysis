

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "Android"
caps["app"] = "/home/dong/Downloads/com.easybrain.sudoku.android_1.3.4-13402_minAPI16(arm64-v8a,armeabi,armeabi-v7a,x86,x86_64)(nodpi)_apkmirror.com.apk"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.implicitly_wait(5)

el1 = driver.find_element_by_id("com.easybrain.sudoku.android:id/btnAccept")
el1.click()
el2 = driver.find_element_by_id("android:id/content")
el2.click()
el2.click()
el3 = driver.find_element_by_id("com.easybrain.sudoku.android:id/skip")
el3.click()
TouchAction(driver).tap(x=412, y=1015).perform()
el4 = driver.find_element_by_id("com.easybrain.sudoku.android:id/button_3")
el4.click()
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/com.easybrain.sudoku.gui.widgets.ControlPanelView/android.widget.LinearLayout/android.widget.LinearLayout[1]/com.easybrain.sudoku.gui.widgets.BadgeImageButton/android.widget.ImageView")
el5.click()
el6 = driver.find_element_by_id("com.easybrain.sudoku.android:id/dc_custom_imge_view")
el6.click()
el7 = driver.find_element_by_id("com.easybrain.sudoku.android:id/dc_information_popup_btn_ok")
el7.click()
el8 = driver.find_element_by_id("com.easybrain.sudoku.android:id/dc_information_btn")
el8.click()

