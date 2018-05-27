# CV

**Complete 90%**

# Main
A CV template using:
* mustache (as template) (`pip install pystache`)
* json (as data source) or yaml
* python (complete CV html output)
* html (as CV output) (or print as PDF later)

For quick output, easy change, independent format.

See the `cv.html` as a [Demo]( https://ffengill.github.io/CV/demo.html).

简历自动生成模版:
* 使用json存储和修改数据
* python结合mustache渲染 （`pip install pystache`安装依赖）
* 输出html作为简历 （也可以执行打印为PDF）

模版清爽，易于修改，简单快速使用。

多说无用，请看[Demo]( https://ffengill.github.io/CV/demo.html).

# Minor
For convenience, add js version using:
* mustache javascript in html
* GET json and template
* render CV in html

so we can quick generate CV:
```
use python http server or others:
python -m SimpleHTTPServer 8888
visit it:
http://localhost:8888
```


添加js版本：
* 使用mustche js版本
* 通过GET获取json数据和template模板
* 在html中渲染CV

这样就有个简单的生成CV的方法了：
```
启用http server（python或者其他皆可）：
python -m SimpleHTTPServer 8888
访问即可：
http://localhost:8888
```

# Misc
Thanks to [prat0318](https://github.com/prat0318/json_resume) for the base work.