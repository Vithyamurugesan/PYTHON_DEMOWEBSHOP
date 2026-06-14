from selenium.webdriver.common.by import By

class ProductReview:

    def __init__(self):
        self.__reviewBtn=(By.XPATH,"//div[@class='product-review-links']/child::a")
        self.__reviewText=(By.XPATH,"//div[@class='center-2']/descendant::div[@class='page-title']")
        self.__reviewTitle=(By.XPATH,"//div[@class='inputs']/child::input[@class='review-title']")
        self.__reviewGText=(By.XPATH,"//div[@class='inputs']/child::textarea[@class='review-text']")
        self.__submitBTN=(By.XPATH,"//div[@class='buttons']/child::input[@type='submit']")
        self.__productReviewSucces=(By.XPATH,"//div[@class='page-body']/child::div[@class='result']")
        self.__reviewFailText=(By.XPATH,"//div[@class='validation-summary-errors']/descendant::li")
    def get_reviw_BTN(self):
        return self.__reviewBtn
        
    def get_review_Text(self):
        return self.__reviewText
        
    def get_review_GText(self):
        return self.__reviewGText
        
    def get_review_submit(self):
        return self.__submitBTN
        
    def get_review_display(self):
        return self.__productReviewSucces
    
    def get_review_title(self):
        return self.__reviewTitle
    
    def get_review_failed(self):
        return self.__reviewFailText