from GologinController.gologin import GoLogin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import selenium

print("version : ", selenium.__version__)

class GologinController():
    def __init__(self, token):
        self.token = token
    
    def create_profile(self, name_profile):
        
        gl = GoLogin({
            "token": self.token,
            })

        self.profile_id = gl.create({
                                "name": name_profile,
                                "os": 'win',
                                "navigator": {
                                    "language": 'en-US',
                                    "userAgent": 'random',
                                    "resolution": '1024x768',
                                    "platform": 'win32',
                                },
                                'proxy': {
                                    'mode': 'none', # Specify 'none' if not using proxy
                                    'autoProxyRegion': 'us' 
                                    # "host": '',
                                    # "port": '',
                                    # "username": '',
                                    # "password": '',
                                },
                                "webRTC": {
                                    "mode": "alerted",
                                    "enabled": True,
                                },
                            })

        profile = gl.getProfile(self.profile_id)
        return self.profile_id
    
    def open_profile(self, port):
        gl = GoLogin({
                    "token": self.token,
                    "profile_id": self.profile_id,
                    "port": port
                    })

        chrome_driver_path = r"C:\Users\Admin\Desktop\Khóa Python Tool\buoi5\GologinController\chromedriver.exe"

        debugger_address = gl.start()
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", debugger_address)
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        driver.get("https://mail.google.com/")
                    
    def reg_gmail(self):
        pass