# web-UI 自动化测试示例

---

## 框架设计

- pytest
- selenium
- POM页面对象模型（Page Object Model）

---

## 目录结构

    common                 ——公共类
    Page                   ——基类
    PageElements           ——页面元素类
    PageObject             ——页面对象类
    TestCase               ——测试用例
    conftest.py            ——pytest胶水文件
    pytest.ini             ——pytest配置文件

---
目录/文件	             说明	                        是否为python包
common	                 这个包中存放的是常见的通用的类	是
config	                 配置文件目录	                是
logs	                 日志目录	 
page	                 对selenium的方法进行深度的封装	是
page_element	         页面元素存放目录	 
page_object	             页面对象POM设计模式	            是
report	                 报告文件目录	 
TestCase	             所有的测试用例集	            是
tools	                 工具类	                        是
conftest.py	             常用目录等	 
pytest.ini	             pytest配置文件	 

## 运行

### 安装依赖

```shell
pip install -r requirements.txt
```

### 执行主文件

* 在项目根目录执行`run_case.py`文件即可运行项目


# allure参数说明


- pytest --alluredir `result-path`
    - --clean-alluredir 清除历史生成记录
- allure generate `result-path`
    - -c 生成报告前删除上一次生成的报告
    - -o 指定生成的报告目录
- allure open `report-path`
