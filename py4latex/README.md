Python highlighting in LaTeX
============================

On Mac:

1, Copy the *.sty file into /usr/local/texlive/2018/texmf-dist/tex/latex
2, run $ sudo texhash

on CentOS:
1, Copy the *.sty file into /usr/share/texlive/texmf-dist/tex/latex
2, run $ sudo texhash

A simple Python highlighting style to be used with LaTeX.

```tex
\usepackage{pythonhighlight}
```

```tex
\begin{python}
def f(x):
    return x
\end{python}
```

```tex
The special method \pyth{__init__}... 
```

```tex
\inputpython{python_file.py}{23}{50}
```
