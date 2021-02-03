# 2021.Feb.01
* project goal:
    * Let news website traffic help e-commerse
* project arch:
    * very large BD API ...
* ML model:
    * tag/persona
    * user vector
    * OneID
    * TPR: Text-aware Preference Ranking
* business value:
    * put ads more precisely
    * redirect traffic to mall

* tools:
    * sonarcloud
    * travis
    * pyspark
    * miro
    * azure databrick
    * asana
## administrative
self-intro\
photo\
need to finish ASUS training\
# 2021.Feb.02
## todo
https://asus-aics.github.io/DeveloperGuide/
https://travis-ci.com/
https://sonarcloud.io/organizations/asus-aics/projects
https://adb-868627275432697.17.azuredatabricks.net/login.html?o=868627275432697#notebook/4188553713246877/command/4188553713246878 OK
## ref
### pyspark sql 
https://spark.apache.org/docs/latest/sql-getting-started.html
https://docs.databricks.com/_static/notebooks/graphframes-user-guide-py.html
## learning note
### 
groupby needs aggregation function 
### 
To create a cell of another language, start the cell with:
    %md - Markdown
    %sql - SQL
    %scala - Scala
    %python - Python
    %r - R
    %sh - Shell
    %fs - Databricks File System
### arpache parquet
https://stackoverflow.com/questions/36822224/what-are-the-pros-and-cons-of-parquet-format-compared-to-other-formats
## 人員分配
	brett 老大
	brian tech lead 在新加坡
	markov 主要是 data scientist，現在在 oneid 這裡做驗證的事情
	chunhunag (我的左邊) 主要是 data factory pipeline 和 release pipeline, production infra 相關的人
	yiying (女生) 主要現在做 oneid 可視化 dashboard 前端，偶爾做一下 dashboard 後端
	jonathan (yiying 對面) data scientist，主要做 user persona PoC 開發
	keanseng 在新加坡，data scientist，一樣做 user persona PoC 開發，好像後續會做性別年齡預測之類的
	vincent 在新加坡，主要是 release pipeline 和 oneid api serivce 開發
## set Github token
https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token

for azure databrick to access github codes
need to know what kind of privilige is required
## aics developer guide
https://asus-aics.github.io/DeveloperGuide/
## want to ask
graph DB ? ok
edge ? ok
vertex? ok
work from home, need vpn to check-in? ok, need, go to set it
F4s L8s: just different VM services provides by Azure
PII table? 
## ROC AUC
Receiver operating characteristic
Area under the curve
# 2021.Feb.03
## pipeline arch
constant
constant
table
partition col: save in diffirent folder

table_transformer will generate table

raw transform

black list 
1st party
3rd party

meta data store

feature store

ua=user agent

user id = KG gave us

prediction with member

user id = KG news
group id = if using same device

predic w/ w/o member

## administrative routines
VPN for work from homw
## python oop
### self vs cls
https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes

Always use self for the first argument to instance methods.

Always use cls for the first argument to class methods.
### @classmethod and classmethod()
https://www.programiz.com/python-programming/methods/built-in/classmethod
#### Factory methods
Factory methods are those methods that return a class object (like constructor) for different use cases.
### class MyClass vs class Myclass(object)
