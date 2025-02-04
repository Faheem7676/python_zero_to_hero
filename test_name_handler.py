from selenium.webdriver.common.by import By

class Commonfunction:
    
    #log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        
        self.driver=driver
    
    
    def getbyType(self,locatorType):
        
        locatorType=locatorType.lower()
        if locatorType=='id':
            
            return By.ID
        
        elif locatorType=="xpath":
            return By.XPATH
        
        elif locatorType=="Name":
            
            return By.NAME
        elif locatorType=="css":
            return By.CSS_SELECTOR
        
        elif locatorType=="linkText":
            return By.LINK_TEXT
        
        else:
            raise ValueError(f"Unsupported locator type:{locatorType}")
            
    
    
    def getElement(self,locator,locatorType='id'):
        
        Element=None
        
        try:
            
            locatorType=locatorType.lower()
            byType=self.getbyType(locatorType)
            Element=self.driver.find_element(byType,locator)
            print("Element found",Element)   
            
        except:
            print("Element not found:", Element)
    
    
    def elementclick(self,locator="",locatorType='id'):
        """code modified for elment click
        
        """
        try:
            if element:
                
                element=self.getElement(locator,locatorType)
            element.click()
            
        except:
            ValueError
        
        