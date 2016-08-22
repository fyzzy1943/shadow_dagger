# auto download the torrent

本程序用来监听网站的种子发布，并自动下载和记录，配合下载软件的目录监控可实现自动下载。

### 首先将.env.simple复制为.env
- name可为自定义名称
- url为rss下载器获得的地址
- dir为种子下载目录

#### windows定时执行执行可导入schtask.xml，导入之前需修改
- `<UserId>计算机名\用户名</UserId>`中的计算机名和用户名为本地实际名称
- `<WorkingDirectory>起始目录</WorkingDirectory>`中的起始目录为程序所在目录，e.g.D:\shadow_dagger
- 之后去任务计划程序中导入即可
- 程序默认为5分钟执行一次

##### 程序执行以后会生成几个文件
- `mission.log`为程序执行日志
- `torrent.db`为下载过的种子记录
- `torrent.log`为下载种子的日志
- `torrent.xml`为获取到的临时rss xml
