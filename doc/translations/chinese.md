# sqlgo

# sqlgo 项目是什么？
sqlgo 是一款专为教育目标进行 SQL 注入测试而设计的工具，并非非法。记住：仅供道德使用！！！

# 如何安装sqlgo？
````
git clone --depth 1 https://github.com/HeisenbergCipherCracker/sqlgo.git
````
将上述命令复制到终端并导航到 sqlgo 目录
确保您的系统上安装了 git。

# 依赖项
- 使用以下命令使用 pip 安装 sqlgo 依赖项
````
pip install -r 要求.txt
````
````
pip3 install -r 要求.txt
````
**适用于 Windows 操作系统**
````
python -m pip install -r requests.txt
````
python3 -m pip install -rrequirements.txt
**对于基于 UNIX 的系统**







**显示帮助菜单**
````
python3 sqlgo.py --update
````

**更新程序**

````
python3 sqlgo.py --help
````

**发起攻击**
````
python3 sqlgo.py -u http://www.target-url?id=1 --level <级别> --verbose <详细> --tamper <tamper> --dbms<DBMS> --dump
````
#sqlgo的特点
1）支持针对MySQL的SQL注入攻击
2) 支持发送不同的有效负载，包括堆栈查询、延时和联合所有有效负载以及其他强有效负载。
3）提供大量篡改脚本来篡改有效负载以绕过WAF或入侵检测系统（IDS）。
4）提供各种编码技术进行编码
5）自动sql注入漏洞检测和扫描器


# 我如何报告错误？
如果存在错误，则将被接受，并且您可以从 sqlgo 的 github 页面报告它。您可以转到 github 中的问题选项卡并以明确的句子报告错误。