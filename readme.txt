pip freeze > requirements.txt
pip install -r requirements.txt

plt.rcParams['font.sans-serif'] = ['SimHei']     # 用来显示中文标签
plt.rcParams['axes.unicode_minus'] = False       # 用来正常显示负号

python安装库的六种方法
方法1： 单文件模块
直接把文件拷贝到 $python_dir/Lib

方法2： 多文件模块，带setup.py
下载模块包（压缩文件zip或tar.gz），进行解压，CMD->cd进入模块文件夹，执行：
python setup.py install

方法3：easy_install 方式
先下载ez_setup.py,运行python ez_setup 进行easy_install工具的安装，之后就可以使用easy_install进行安装package（文件名称、资源的URL、.egg文件（python egg文件）来下载安装文件）
easy_install packageName
easy_install package.egg

方法4：pip 网络搜索自动安装
先进行pip工具的安裝：easy_install pip（pip 可以通过easy_install 安裝，而且也会装到 Scripts 文件夹下D:\Python2.7\Lib\site-packages）

安裝：pip install PackageName

pip常用命令
列出安装的packages:pip freeze
安装特定版本的package:通过使用==, >=, <=, >, <来指定一个版本号
$ pip install ‘Markdown<2.0’
$ pip install ‘Markdown>2.0,<2.0.3’
升级包到当前最新的版本，可以使用-U或者–upgrade:
升级包pip install -U Markdown
卸载包：pip uninstall Markdown
查询包：pip search “Markdown”

方法5：.whl文件pip 方式
下载对应模块.whl文件，在CMD->cd命令下进入到.whl文件所在目录，如果pip目录未添加到环境变量，最好把.whl文件放置到pip.exe所在目录（D:\Python2.7\Scripts\）。

安装： pip install 包名.whl

方法6：.exe文件自定义安装
下载对应版本的exe安装文件，如numpy-1.9.2-win32-superpack-python2.7.exe和mlpy-3.5.0.win32-py2.7.exe
安装：打开自动安装即可
