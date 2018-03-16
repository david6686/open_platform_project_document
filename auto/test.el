(TeX-add-style-hook
 "test"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "12pt" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("xeCJK" "slantfont" "boldfont")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "xltxtra"
    "fontspec"
    "xunicode"
    "xeCJK"))
 :latex)

