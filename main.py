from appium import webdriver
import time

default_capabilities = {
  "platformName": "Android",
  "appActivity": "com.atg.world.activity.SplashActivity",
  "appWaitDuration": "5000",
  "appExecTimeout": "50000",
  "uiautomator2ServerLaunchTimeout": "50000",
  "uiautomator2ServerInstallTimeout": "50000",
  "appPackage": "com.ATG.World",
  "deviceName": "emulator-5554",
  "driver": "http://localhost:4723/wd/hub"
}
#####################################
driver = webdriver.Remote("http://localhost:4723/wd/hub", default_capabilities)
driver.implicitly_wait(20)

#####################################

driver.find_element('id','com.android.packageinstaller:id/permission_allow_button').click()
driver.implicitly_wait(10)

#####################################

driver.find_element('id','com.ATG.World:id/getStartedTv').click()
driver.implicitly_wait(10)

#####################################

driver.find_element('id','com.ATG.World:id/login_email').click()

#####################################

driver.find_element('id',"com.ATG.World:id/email_phone_login").send_keys('jayzobalia44@gmail.com')
driver.find_element('id','com.ATG.World:id/signinbutton').click()
time.sleep(2)

#####################################

driver.find_element('id',"com.ATG.World:id/password").send_keys('J@y447506003943')
driver.back()
time.sleep(2)
driver.find_element('id','com.ATG.World:id/passwordloginbutton').click()
driver.implicitly_wait(3)

#####################################

driver.find_element('id','com.ATG.World:id/btnGotit').click()
driver.implicitly_wait(5)

#####################################

driver.find_element('id','com.ATG.World:id/fab').click()
driver.implicitly_wait(5)

#####################################

driver.find_element('id','com.ATG.World:id/image_fab_clicked').click()
driver.implicitly_wait(5)

#####################################

driver.find_element('id','com.ATG.World:id/image_cell').click()
driver.implicitly_wait(5)

#####################################

driver.find_element('id','com.ATG.World:id/image_cell').click()
driver.implicitly_wait(5)

#####################################

driver.find_element('id','com.ATG.World:id/toolbar_post_action').click()
driver.implicitly_wait(5)

#####################################

driver.find_element('id',"com.ATG.World:id/caption_edit_text").send_keys('My First Post via Appium')
driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]').click()
driver.find_element('id','com.ATG.World:id/selection_done_btn').click()

#####################################

print("Automation Posting Completed")