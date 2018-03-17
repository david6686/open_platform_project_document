![Alt latex:xetex](https://img.shields.io/badge/latex-xetex-green.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)

使用說明
==========
主要更改文件為`documnet.tex` (目前只有這個檔案才會被ci轉成pdf)  
此專案已經有使用CI，會自動生成pdf  
(要找生成的pdf要去`CI > pipeline `在最新的pipeline上找下載按鈕)  

>但是目前ci不能編譯中文，所以pipeline會fail  QQ

## 格式
請使用latex格式撰寫
### 中文支援
目前latex檔案
``` latex
% 檔案的首
\usepackage{xltxtra,fontspec,xunicode}
\usepackage[slantfont,boldfont]{xeCJK} % 允许斜体和粗体
\setCJKmainfont{Kai}   % 设置缺省中文字体
\setCJKmonofont{Hei}   % 设置等宽字体
\setmainfont{Optima}   % 英文衬线字体
\setmonofont{Monaco}   % 英文等宽字体
\setsansfont{Trebuchet MS} % 英文无衬线字体


%檔案的尾
%%% Local Variables:
%%% mode: latex
%%% TeX-command-extra-options: "-shell-escape"
%%% TeX-master: t
%%% Tex-coding: utf-8
%%% TeX-engine: xetex
%%% End:


```
