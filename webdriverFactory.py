from selenium import webdriver


class WebdriverFactory():
    
    
    
    def __init__(self,browser):
        
        self.browser=browser
        
    
    def getWebDriverInstance(self):
        
        baseURL="testingqa.com/"
        
        if self.browser=="iexplore":
            
            #set ie driver
            driver=webdriver.Ie
            
        if self.browser=="chrome":
            
            driver=webdriver.Chrome()
            driver.set_window_size(1400,900)
            
        if self.browser=="Firefox":
            
            driver=webdriver.Firefox()
            
        else:
            driver=webdriver.Chrome()
            
        driver.implicitly_wait()
        driver.maximize_window()
        driver.get(baseURL)
        return driver
        
        
        
        
        