# PyLaTex
A php-like way to generate latex documents.

The present PyLaTeX aims to ease the redaction of LaTeX documents based on data that can either be generated or accessed on a data base. Typical use cases include :
* update of the result(s) section(s) of a report
* generation of file "on demande"
* generation of historic (academic transcript, ...)
* generation of assignment correction (see example below)

The present project differs from other projects based on Python as, here, Python is embedded a LaTeX file whereas, in the other projects such as [JelteF/PyLaTeX](https://github.com/JelteF/PyLaTeX), Python is directly used to generate all the LaTeX document.

## Example
```latex
\documentclass[a4paper,11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}

\begin{document}

<?
def reformat(string):
    return string[2:]

ex = [12, 78, 24, 9, 152]
out("%"+str(ex))
?>

\section{Correction exercice 1}
\begin{center}
\begin{tabular}{|c|c|c|}
\hline
dec & bin & hex \\
\hline
<?
for e in ex:
    out(str(e)+" & "+reformat(bin(e))+" & "+reformat(hex(e))+" \\ \n")
    out("\hline \n")
?>
\end{tabular}
\end{center}

\end{document}
```
