from common.base import Base
from common.config import host
import allure
import time

class ArticlclassifyPage(Base):
    客户管理 = ("xpath", '//*[@id="app"]/div/section/aside/div[2]/ul/li[1]/div/span')

    子集_客户管理 = ("xpath", '//*[@id="app"]/div/section/aside/div[2]/ul/li[1]/ul/li/ul/li[1]')
    点击_详情 = ("xpath",
             '//*[@id="app"]/div/section/section/div/main/div/div[2]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[10]/div/button[1]/span')

    # 判断元素
    table = ("xpath", '//*[@id="app"]/div/section/section/div/main/div/div/div[1]/div[2]/table/thead/tr/th[3]/div')

    @allure.step("步骤：点击左侧客户管理导航")
    def click_classify_nav(self):
        '''点击左侧客户管理导航'''
        self.click(self.客户管理)

    @allure.step("步骤：点击详情按钮")
    def edit_classify(self):
        '''点击详情按钮'''
        self.click(self.子集_客户管理)
        self.click(self.点击_详情)

    @allure.step("步骤：判断是否跳转详情页面成功，返回布尔值")
    def is_edit_classify_success(self):
        '''判断是否添加成功，返回布尔值'''
        result = self.is_element_exist(self.table)
        return result

