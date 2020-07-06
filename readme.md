# skyTransformer
很喜欢光遇这款游戏，在游戏里演奏乐器的喜悦之情十分强烈。然而本人手残且未经专业训练，吹奏乐器时总是出错，受UP主格子谱的启发，写了这个小工具，至少可以弹出一定的曲调了。

[中文Readme](#) | [English Readme](#)

## 功能特性

### web version
未实现

### python version
1. 支持的乐谱文件格式:
   * txt (本项目私有格式)
2. 支持输出格子谱
3. 支持格子谱内同时刻多音符，但输出的格子谱不含节拍信息


## 安装

### web version
未实现

### python version
需要自行安装python，Mac及Linux应该有自带的python安装，Windows需要自己手动安装。以下的安装教程默认都拥有python环境（在日后的版本中增加打包功能）
```
pip install virtualenv

virtualenv venv

pip install -r requirements.txt
```

## 效果
小星星的选段
![twinkle twinkle little star](https://github.com/Heersin/skyTransformer/blob/master/python/src/output/music.png)


## 快速上手
```
查看支持的格式:
  python main.py -l

查看示例用法
  python main.py -s

查看命令帮助
  python main.py -h

转换（在output路径下可查看结果）
  python main.py -i test/test_origin  默认输出图片
or
  python main.py -i test/test_origin -o test.png 输出图片
or
  python main.py -i test/test_origin -o test.txt 输出文本（命令行效果）
```

## 用法
```
usage: main.py [-h] [-l | -s] [-i INPUT_FILE] [-o OUTPUT]

Sky Notation Tranformer

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            list support formats
  -s, --show            show usage example
  -i INPUT_FILE, --input_file INPUT_FILE
                        input file name
  -o OUTPUT, --output OUTPUT
                        output file name(no path)
```

## 依赖项
Pass

## 开发指南
### 项目结构
```sh
skytransformer
	|
	|----- python
	|		|----src
	|			  | --- skyEncoder (encoder package)
	|			  | --- skyDecoder (decoder package)
	|			  | --- skyDisplayer (displayer package)
	|			  | --- test/
	|          	  | --- skytransformer (the main programe)
	|		|----venv/ (可选，推荐在这里放虚拟环境)
	|		|----output/ (输出的文件)
	|
	|----- Web
			|----TODO/
```
### 项目原理
整个项目遵循Encode - Decode - Display这样的流程，其中每个步骤处理事项如下
* Encode : 由skyEncoder Module完成，负责对不同数据格式的读入和处理，最终encode成统一的音符格式
* Decode: 由skyDecoder Module完成，负责对经过encode的统一格式进行处理，完成音符到对应格子谱坐标的转换
* Display; 由skyDisplayer Module完成，决定如何对这些坐标进行可视化，例如，我提供了命令行的输出格式以及图片的输出显示。

这三个模块都可以通过继承对应基类并实现接口自行实现，以适应不同场景。例如，可以实现不同的decoder，以满足对不同文件格式的处理需求，若将来光遇增加新的音高，则更新encoder模块，输出格式目前以完整图片输出为主，命令行输出(<del>也就图一乐</del>)主要是在没有桌面的环境中使用，以及debug中测试前两个模块的可靠性。

### 开发文档
[开发文档在这里(无)](#)
## 贡献
感谢使用本项目，欢迎在issue区提出想增加的功能，也可以反映bug。或者可以发送到我的邮箱teablearcher@gmail.com

