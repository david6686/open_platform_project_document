![Alt latex:xetex](https://img.shields.io/badge/latex-xetex-green.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)
![Alt ci compiler fail](https://img.shields.io/teamcity/http/teamcity.jetbrains.com/s/bt345.svg)

使用說明
==========
主要更改文件為`documnet.tex` (目前只有這個檔案才會被ci轉成pdf)  
此專案已經有使用CI，會自動生成pdf  
(要找生成的pdf要去`CI > pipeline `在最新的pipeline上找下載按鈕)  

>但是目前ci不能編譯中文，所以pipeline會fail  QQ

## 格式
請使用latex格式撰寫
### 中文支援
[參考](https://liam0205.me/2014/11/02/latex-mactex-chinese-support/)   

目前latex檔案
``` tex
% 檔案的首
\usepackage{xltxtra,fontspec,xunicode}
\usepackage[slantfont,boldfont]{xeCJK} % 允许斜体和粗体
\setCJKmainfont{STSongti-TC-Regular} % 繁體標準宋體  如果碰到字體問題  加油   找系統字體本找能用的
% \setCJKmainfont{Kai}   % 设置缺省中文字体  原本應該是通用的標楷體 會有方塊字問題
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
## latex環境安裝
### spacemacs（如果不寫某大神可能會把我滅了）
1. 安裝[emacs](https://www.gnu.org/software/emacs/)  （歡迎，神級編輯器）
2. 安裝[spacemacs](http://spacemacs.org)
3. 安裝[Tex liev](https://www.tug.org/texlive/)
4. 為你的spacemacs安裝 [latex layer](https://github.com/syl20bnr/spacemacs/tree/master/layers/%2Blang/latex) （還好還好，設定檔加個5,6行 咳咳）
5. 把你的spacemacs latex engine改成xeletex ([教學](https://emacs-china.org/t/topic/293) 參考倒數第二樓的設定，與三樓latex文章尾部設定)
6. 開啟你的`Tex live unity`
7. 開啟你的`TexShop`去 `設定>source>code 改成utf-8`（[參考](https://liam0205.me/2014/11/02/latex-mactex-chinese-support/)）
8. 大概配置完了...使用`神器spacemacs`開啟tex檔案，使用`SPC m b `編譯，如果說PATH問題（[solve](https://apple.stackexchange.com/questions/277928/error-auctex-cannot-find-a-working-tex-distribution-macos-sierra)）
9. 然後...應該...沒有問題了(眼神死)   

### visual studio + latex workflow
[參考](https://www.jianshu.com/p/57f8d1e026f5)  
1. 輕輕開啟你的`visual studio`
2. ~~然後重重的解除安裝去使用emacs~~ 安裝擴充套件`latex-workflow`,`latex language support`
3. 安裝[Tex liev](https://www.tug.org/texlive/)
4. 開啟你的`Tex live unity`
5. 開啟你的`TexShop`去 `設定>source>code` 改成utf-8（[參考](https://liam0205.me/2014/11/02/latex-mactex-chinese-support/)）
6. `visual studio`覆蓋設定
```
"latex-workshop.latex.toolchain": [
        {
          "command": "xelatex",
          "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOC%"
          ]
        }
      ]
```

7. 使用visual studio開啟.tex 右鍵選擇`build latex project`
8. 應該就會有可愛的pdf出現了  大概

------------------


## 編譯器勢力圖（舊）
![Alt hahaha](https://github.com/emacs-tw/emacs-101-beginner-survival-guide/raw/master/pic/alliances_zh.png)  


