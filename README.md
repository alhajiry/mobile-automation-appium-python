This mobile automation framework contains test cases to test Blibli Android application. 
Blibli is B2C ecommerce developed by Indonesian company and operating in Indonesian market. 

To run the test, you need to have an Android emulator/physical device with Blibli application installed. The Blibli Android application can be downloaded from Playstore : [Blibli Android Playstore](https://play.google.com/store/apps/details?id=blibli.mobile.commerce&hl=id)

If there is a need to change the device for testing, you can change it by changing the ```options.device_name``` in the code below
https://github.com/alhajiry/mobile-automation-appium-python/blob/087757bfaff2655d57d46d7bc74db885483dc66f/base_driver.py#L8-L16

In order to run the test, you need to have python with version 3.13.1 installed
For Windows, you can download it in here : https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe

Install the required depedencies
```
pip install -r requirements.txt
```

Run the test using this command
```
Run using command 'pytest'
```

*Please note that this framework is built using Windows machine, for Linux/MacOS there could be an adjustment needed.

If there is any question please mail me at [al.hajiry16@gmail.com](mailto:al.hajiry@gmail.com?subject=[GitHub]%20Appium%20Python%20Automation%20Framework)
