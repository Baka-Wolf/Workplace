# 这是我照抄Markdown教程的本地化教程

[原文](https://markdown.com.cn/intro.html)

# 标题的语法

># 这是一级标题
>
>`# 这是一级标题`
>
>## 这是二级标题
>
>`## 这是二级标题`
>
>### 这是三级标题
>
>`### 这是三级标题`
>
>#### 这是四级标题
>
>`#### 这是四级标题`
>
>##### 这是五级标题
>
>`##### 这是五级标题`
>
>###### 这是六级标题
>
>`###### 这是六级标题`

>这是正文

不同的 Markdown 应用程序处理 # 和标题之间的空格方式并不一致。为了兼容考虑，请用一个空格在 # 和标题之间进行分隔。

# 段落的语法

要创建段落，请使用空白行将一行或多行文本进行分隔。

不要用空格（spaces）或制表符（ tabs）缩进段落。

# 换行的语法

在一行的末尾添加两个或多个空格，然后按回车键,即可创建一个换行。  <br>
就像这样  
哦

几乎每个 Markdown 应用程序都支持两个或多个空格进行换行，称为 结尾空格（trailing whitespace) 的方式，但这是有争议的，因为很难在编辑器中直接看到空格，并且很多人在每个句子后面都会有意或无意地添加两个空格。由于这个原因，你可能要使用除结尾空格以外的其它方式来换行。幸运的是，几乎每个 Markdown 应用程序都支持另一种换行方式：HTML 的 `<br>` 标签。

为了兼容性，请在行尾添加“结尾空格”或 HTML 的 `<br>` 标签来实现换行。

还有两种其他方式我并不推荐使用。CommonMark 和其它几种轻量级标记语言支持在行尾添加反斜杠 (`\`) 的方式实现换行，但是并非所有 Markdown 应用程序都支持此种方式，因此从兼容性的角度来看，不推荐使用。并且至少有两种轻量级标记语言支持无须在行尾添加任何内容，只须键入回车键（`return`）即可实现换行。

# 强调的语法

### 粗体

通过将文本设置为粗体或斜体来强调其重要性。<br>
要加粗文本，请在单词或短语的前后各添加两个星号（asterisks，`*`）或下划线（underscores，`_`）。如需加粗一个单词或短语的中间部分用以表示强调的话，请在要加粗部分的两侧各添加两个星号（asterisks，`*`）。

Markdown 应用程序在如何处理单词或短语中间的下划线上并不一致。为兼容考虑，在单词或短语中间部分加粗的话，请使用星号（asterisks）。

### 斜体

要用斜体显示文本，请在单词或短语前后添加一个星号（asterisk，`*`）或下划线（underscore，`_`）。要斜体突出单词的中间部分，请在字母前后各添加一个星号，中间不要带空格。

要同时用粗体和斜体突出显示文本，请在单词或短语的前后各添加三个星号或下划线。要加粗并用斜体显示单词或短语的中间部分，请在要突出显示的部分前后各添加三个星号，中间不要带空格。

Markdown 应用程序在处理单词或短语中间添加的下划线上并不一致。为了实现兼容性，请使用星号将单词或短语的中间部分加粗并以斜体显示，以示重要。

# 引用的语法

要创建块引用，请在段落前添加一个 `>` 符号。<br>
效果如下：
>这是示例。

块引用可以嵌套。在要嵌套的段落前添加一个 `>>` 符号。
>著名作家鲁迅曾说过：<br>
>>“说的什么叽里呱啦的我忘了。”

块引用可以包含其他 Markdown 格式的元素。并非所有元素都可以使用，你需要进行实验以查看哪些元素有效。

    > #### 他知道我们爱他么？这个宇宙是仁慈的？
    >
    > - 有时，通过他思绪的杂音，他能听到宇宙，是的。
    > - 但是有时亦不胜悲伤，于那漫漫长梦中。他创造了没有夏日的世界，在黑日下颤抖着，将自己悲伤的创造视为现实世界。
    >
    >  用*悲伤*来治愈会摧毁他。而悲伤是他的私人事务。我们**不能**干涉。
效果如下：
> #### 他知道我们爱他么？这个宇宙是仁慈的？
>
> - 有时，通过他思绪的杂音，他能听到宇宙，是的。
> - 但是有时亦不胜悲伤，于那漫漫长梦中。他创造了没有夏日的世界，在黑日下颤抖着，将自己悲伤的创造视为现实世界。
>
>  用*悲伤*来治愈会摧毁他。而悲伤是他的私人事务。我们**不能**干涉。

# 列表的语法

可以将多个条目组织成有序或无序列表。

### 有序列表

要创建有序列表，请在每个列表项前添加数字并紧跟一个英文句点。数字不必按数学顺序排列，但是列表应当以数字 1 起始。

    1. First item
    2. Second item
    3. Third item
    4. Fourth item 

同时  

    1. First item
    2. Second item
    3. Third item
        1. Indented item
        2. Indented item
    4. Fourth item

### 无序列表

要创建无序列表，请在每个列表项前面添加破折号 (-)、星号 (*) 或加号 (+) 。缩进一个或多个列表项可创建嵌套列表。

    - First item
    - Second item
    - Third item
    - Fourth item
- First item
- Second item
- Third item
- Fourth item

同时

    - First item
    - Second item
    - Third item
        - Indented item
        - Indented item
    - Fourth item
- First item
- Second item
- Third item
    - Indented item
    - Indented item
- Fourth item

要在保留列表连续性的同时在列表中添加另一种元素，请将该元素缩进四个空格或一个制表符，如下例所示：

    - 这是例子
    - 这也是例子

        哈？

    - 这是例子

- 这是例子
- 这也是例子

    哈？

- 这是例子 

还可以加入引用块。

    - 这是例子
    - 这也是例子

        >哈？

    - 这是例子

- 这是例子
- 这也是例子

    >哈？

- 这是例子 

代码块通常采用四个空格或一个制表符缩进。当它们被放在列表中时，请将它们缩进八个空格或两个制表符。

### 插入图片的列表

- **（前置知识：图片的语法）**

    1. 打开图片
    2. 哎我去真是萌萌哒啊

        `![原石龙 帝王黄玉龙](/assets/img/Primite_Imperial_Dragon.jpg)`

    3. 关掉图片

1. 打开图片
2. 哎我去真是萌萌哒啊

    ![原石龙 帝王黄玉龙](/assets/img/Primite_Imperial_Dragon.jpg)

3. 关掉图片

# 代码的语法

要将单词或短语表示为代码，请将其包裹在反引号 ( ` ) 中。

如果你要表示为代码的单词或短语中包含一个或多个反引号，则可以通过将单词或短语包裹在双反引号(``)中。

要创建代码块，请将代码块的每一行缩进至少四个空格或一个制表符。

    我是代码

``我也是代码``

# 分隔线的语法

要创建分隔线，请在单独一行上使用三个或多个星号 (`***`)、破折号 (`---`) 或下划线 (`___`) ，并且不能包含其他内容。

以上三个分隔线的渲染效果看起来都一样：

 ***
 ---
 ___

为了兼容性，请在分隔线的前后均添加空白行。

    ***

    这是内容

    ***

# 链接的语法

链接文本放在中括号内，链接地址放在后面的括号中，链接title可选。

超链接Markdown语法代码：`[超链接显示名](超链接地址 "超链接title")`

对应的HTML代码：`<a href="超链接地址" title="超链接title">超链接显示名</a>`

[大粪聚集处](https://github.com/Baka-Wolf/Workplace)

包含链接title的效果如下：

[大粪聚集处](https://github.com/Baka-Wolf/Workplace "超乎你想象的屎山代码")

这样，在光标悬浮于链接时便会显示title。

使用尖括号可以很方便地把URL或者email地址变成可点击的链接。

    <https://github.com/Baka-Wolf/Workplace>
    <bakawolf114514@gmail>

<https://github.com/Baka-Wolf/Workplace><br>
<bakawolf114514@gmail.com>

 要将链接表示为代码，请在方括号中添加反引号。

[`大粪聚集处`](https://github.com/Baka-Wolf/Workplace)

不同的 Markdown 应用程序处理URL中间的空格方式不一样。为了兼容性，请尽量使用%20代替空格。

### 引用类型链接

引用样式链接是一种特殊的链接，它使URL在Markdown中更易于显示和阅读。参考样式链接分为两部分：与文本保持内联的部分以及存储在文件中其他位置的部分，以使文本易于阅读。

##### 第一部分

引用类型的链接的第一部分使用两组括号进行格式设置。第一组方括号包围应显示为链接的文本。第二组括号显示了一个标签，该标签用于指向您存储在文档其他位置的链接。

尽管不是必需的，可以在第一组和第二组括号之间包含一个空格。第二组括号中的标签不区分大小写，可以包含字母，数字，空格或标点符号。

以下示例格式对于链接的第一部分效果相同：

[hobbit-hole][1]

[hobbit-hole] [1]

##### 第二部分

引用类型链接的第二部分使用以下属性设置格式：

- 放在括号中的标签，其后紧跟一个冒号和至少一个空格（例如`[label]:`）。
- 链接的URL，可以选择将其括在尖括号中。
- 链接的可选标题，可以将其括在双引号，单引号或括号中。

以下示例格式对于链接的第二部分效果相同：

    [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
    [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
    [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"
    [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> 'Hobbit lifestyles'
    [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> (Hobbit lifestyles)

[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"
[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> 'Hobbit lifestyles'
[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> (Hobbit lifestyles)

可以将链接的第二部分放在Markdown文档中的任何位置。有些人将它们放在出现的段落之后，有些人则将它们放在文档的末尾（例如尾注或脚注）。

# 图片的语法

要添加图像，请使用感叹号 (`!`), 然后在方括号增加替代文本，图片链接放在圆括号里，括号里的链接后可以增加一个可选的图片标题文本。

插入图片Markdown语法代码：`![图片alt](图片链接 "图片title")`。

对应的HTML代码：`<img src="图片链接" alt="图片alt" title="图片title">`

给图片增加链接，请将图像的 Markdown 括在方括号中，然后将链接添加在圆括号中。

    [![原石龙 帝王黄玉龙](/assets/img/Primite_Imperial_Dragon.jpg "Primite Imperial Dragon")](https://ygocdb.com/card/81418467)

[![原石龙 帝王黄玉龙](/assets/img/Primite_Imperial_Dragon.jpg "Primite Imperial Dragon")](https://ygocdb.com/card/81418467)

# 转义字符的语法

要显示原本用于格式化 Markdown 文档的字符，请在字符前面添加反斜杠字符 `\` 。

    \*这是例子
\*这是例子

在 HTML 文件中，有两个字符需要特殊处理： `<` 和 `&` 。 `<` 符号用于起始标签，`&` 符号则用于标记 HTML 实体，如果你只是想要使用这些符号，你必须要使用实体的形式，像是 `&lt`; 和 `&amp`;。

`&` 符号其实很容易让写作网页文件的人感到困扰，如果你要打「AT&T」 ，你必须要写成「`AT&amp;T`」 ，还得转换网址内的 `&` 符号，如果你要链接到：

    http://images.google.com/images?num=30&q=larry+bird

你必须写成：

    http://images.google.com/images?num=30&amp;q=larry+bird

才能放到链接标签的 href 属性里。不用说也知道这很容易忘记，这也可能是 HTML 标准检查所检查到的错误中，数量最多的。

Markdown 允许你直接使用这些符号，它帮你自动转义字符。如果你使用 `&` 符号的作为 HTML 实体的一部分，那么它不会被转换，而在其它情况下，它则会被转换成 `&amp`;。所以你如果要在文件中插入一个著作权的符号，你可以这样写：

    &copy;

Markdown 将不会对这段文字做修改，但是如果你这样写：

    AT&T

Markdown 就会将它转为：

    AT&amp;T

类似的状况也会发生在 `<` 符号上，因为 Markdown 支持行内 HTML ，如果你使用 `<` 符号作为 HTML 标签的分隔符，那 Markdown 也不会对它做任何转换，但是如果你是写：

    4 < 5

Markdown 将会把它转换为：

    4 &lt; 5

需要特别注意的是，在 Markdown 的块级元素和内联元素中， `<` 和 `&` 两个符号都会被自动转换成 HTML 实体，这项特性让你可以很容易地用 Markdown 写 HTML。（在 HTML 语法中，你要手动把所有的 `<` 和 `&` 都转换为 HTML 实体。）

# 内嵌 HTML 标签的语法

对于 Markdown 涵盖范围之外的标签，都可以直接在文件里面用 HTML 本身。如需使用 HTML，不需要额外标注这是 HTML 或是 Markdown，只需 HTML 标签添加到 Markdown 文本中即可。

HTML 的行级內联标签如 `<span>`、`<cite>`、`<del>` 不受限制，可以在 Markdown 的段落、列表或是标题里任意使用。依照个人习惯，甚至可以不用 Markdown 格式，而采用 HTML 标签来格式化。例如：如果比较喜欢 HTML 的 `<a>` 或 `<img>` 标签，可以直接使用这些标签，而不用 Markdown 提供的链接或是图片语法。当你需要更改元素的属性时（例如为文本指定颜色或更改图像的宽度），使用 HTML 标签更方便些。

HTML 行级內联标签和区块标签不同，在內联标签的范围内， Markdown 的语法是可以解析的。

区块元素──比如 `<div>`、`<table>`、`<pre>`、`<p>` 等标签，必须在前后加上空行，以便于内容区分。而且这些元素的开始与结尾标签，不可以用 tab 或是空白来缩进。Markdown 会自动识别这区块元素，避免在区块标签前后加上没有必要的 `<p>` 标签。

请注意，Markdown 语法在 HTML 区块标签中将不会被进行处理。例如，你无法在 HTML 区块内使用 Markdown 形式的`*强调*`。

出于安全原因，并非所有 Markdown 应用程序都支持在 Markdown 文档中添加 HTML。如有疑问，请查看相应 Markdown 应用程序的手册。某些应用程序只支持 HTML 标签的子集。

对于 HTML 的块级元素 `<div>`、`<table>`、`<pre>` 和 `<p>`，请在其前后使用空行（blank lines）与其它内容进行分隔。尽量不要使用制表符（tabs）或空格（spaces）对 HTML 标签做缩进，否则将影响格式。

在 HTML 块级标签内不能使用 Markdown 语法。例如 `<p>italic and **bold**</p>` 将不起作用。