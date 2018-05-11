(TeX-add-style-hook
 "test"
 (lambda ()
   (setq TeX-command-extra-options
         "-shell-escape")
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "UTF8" "12pt" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("hyperref" "colorlinks" "linkcolor=black" "urlcolor=blue") ("xeCJK" "slantfont" "boldfont")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "xltxtra"
    "fontspec"
    "xunicode"
    "graphicx"
    "hyperref"
    "xeCJK"))
 :latex)

