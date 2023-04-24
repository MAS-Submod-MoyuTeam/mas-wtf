<h1 align="center">🔍 Where is That From</h1>
<h3 align="center">超简单就找到这个话题是谁添加的!</h3>
<h5 align="center">啊对对，它的简称就是wtf.</h5>

<p align="center">
  <a href="https://github.com/friends-of-monika/mas-wtf/releases/latest">
    <img alt="Latest release" src="https://img.shields.io/github/v/release/friends-of-monika/mas-wtf">
  </a>
  <a href="https://github.com/friends-of-monika/mas-wtf/releases">
    <img alt="Release downloads" src="https://img.shields.io/github/downloads/friends-of-monika/mas-wtf/total">
  </a>
  <a href="https://www.reddit.com/r/MASFandom/comments/10jg4bc/where_is_that_from_submod_release_introduction">
    <img alt="Reddit badge" src="https://img.shields.io/badge/dynamic/json?label=%F0%9D%97%8B%2FMASFandom&query=%24[0].data.children[0].data.score&suffix=%20upvotes&url=https%3A%2F%2Fwww.reddit.com%2Fr%2FMASFandom%2Fcomments%2F10jg4bc%2Fwhere_is_that_from_submod_release_introduction.json&style=social&logo=reddit">
  </a>
  <a href="https://github.com/friends-of-monika/mas-wtf/blob/main/LICENSE.txt">
    <img alt="MIT license badge" src="https://img.shields.io/badge/License-MIT-lightgrey.svg">
  </a>
  <a href="https://dcache.me/discord">
    <img alt="Discord server" src="https://discordapp.com/api/guilds/1029849988953546802/widget.png?style=shield">
  </a>
  <a href="https://ko-fi.com/Y8Y15BC52">
    <img alt="Ko-fi badge" src="https://ko-fi.com/img/githubbutton_sm.svg" height="20">
  </a>
</p>


## 🌟 特性

对于那些热衷于尝试新的子模组并且可能需要帮助找到某个特定主题来源的人来说，这是一个真正必备的工具！

* 区分官方主题和子模组主题
* 提供当前主题名称的信息
* 显示所有者子模组名称和脚本文件位置

## ❓ 安装

1. 前往[Releases][6]，滚动到Assets部分。
2. 下载 `where-is-that-from-VERSION.zip` 文件。
3. 从中拖放`Submods`文件夹到你的`game`文件夹中。
4. 安装完成！~

### 📚 如何使用？

每当您需要找到您当前正在查看的主题的位置以及它所属的子模组时，按下`W`键或`？`（问号，可能需要按住`Shift⬆`键），弹出对话框窗口将向您提供所有可用的信息。

### 🙋 常见问题解答

*长话短说，归咎于Ren'Py。 不要归咎于MAS，也不要归咎于MAS开发人员或WTF开发人员，归咎于Ren'Py的设计选择不佳。*

#### 🤔 为什么使用“似乎”和“可能”这样的不确定性词语？

不幸的是，目前没有一种可靠的直接的编程方法来确定Ren'Py正在使用哪个文件来显示某个特定主题；为了解决这个问题，Where is That From 子模组使用了一些技巧，但这些技巧并不总是可靠且准确。

此外，无法确定当前主题是否在您完成它后仍将可访问，因为它可能在最后执行某些锁定逻辑，而且无法确定它是否肯定会再次访问。很抱歉带来的不确定性，但它只能做到这样...

#### 🤔 为什么它无法检测到所属主题的子模组？

由于Ren'Py的工作方式和MAS处理事件的方式，无法确定某个主题是否属于具有某些子模组元数据的文件。Where is That From子模组尝试在当前主题文件中搜索子模组元数据，如果没有找到，它也可以尝试在相邻文件中查找。然而，在将.RPY/.RPYC文件放置在`game`或`game/Submods`而不是其自己的文件夹中的情况下，搜索范围太广，它不能在没有高风险误报的情况下查找周围文件并确定所属的子模组头。

另外，子模组开发人员可能会因自己的原因省略声明文件，这会阻止Where is That From子模组确定提供脚本文件的子模组。但它至少可以告诉您当前正在查看的主题所在的文件。

## 💬 加入我们的Discord

我们欢迎交流！来加入子模组作者的[Discord服务器][8]。

[![Discord server invitation][10]][8]

[6]: https://github.com/MAS-Submod-MoyuTeam/mas-wtf/releases/latest
[8]: https://dcache.me/discord
[9]: https://mon.icu/discord
[10]: https://discordapp.com/api/guilds/1029849988953546802/widget.png?style=banner3
[12]: https://github.com/friends-of-monika/mas-wtf
