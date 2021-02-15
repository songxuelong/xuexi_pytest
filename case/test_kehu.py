# -*- coding: utf-8 -*-
import pytest
from pages.articleclassify_page import ArticlclassifyPage
import allure

from common.read_yml import readyml

'''
allure对用例的等级划分成五个等级
 blocker　 阻塞缺陷（功能未实现，无法下一步）
 critical　　严重缺陷（功能点缺失）
 normal　　 一般缺陷（边界情况，格式错误）
 minor　 次要缺陷（界面错误与ui需求不符）
 trivial　　 轻微缺陷（必须项无提示，或者提示不规范）
'''


@allure.feature("客户管理")
class TestArticleclassify():
    @allure.severity("critical")
    @allure.title("编辑文章分类，输入中文，编辑成功")
    def test_add_article1(self, login):
        '''用例描述：1.先登陆
        点客户管理导航标签
        点击详情安妮'''
        driver = login
        edit = ArticlclassifyPage(driver)
        edit.click_classify_nav()
        edit.edit_classify()
        res2 = edit.is_edit_classify_success()
        assert res2

