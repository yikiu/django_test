配置：
install.sh中env_path值为virtualenv安装的python虚拟路径。启动服务前，需要修改uwsgi_*.ini中home为env_path指向的路径。
nginx配置
server中的location中增加以下两句：
 uwsgi_pass 127.0.0.1:8761;
 include uwsgi_params;

uwsgi_pass 后的ip为运行服务的ip,端口号为uwsgi_*.ini中"socket=127.0.0.1:8761"指定的端口号，此处为8761.

init.sh 用于安装virtualenvwrapper环境，每个系统只需要执行一次
install.sh用于设置工程运行环境

数据库、redis配置信息在mysql_redis.cg 中设置。
本地测试数据库、config/settings/local.py中设置。

