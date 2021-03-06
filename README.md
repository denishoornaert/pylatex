# PyLaTex
A php-like way to generate latex documents.

The present PyLaTeX aims to ease the redaction of LaTeX documents based on data that can either be generated or accessed on a data base. Typical use cases include :
* update of the result(s) section(s) of a report
* generation of file "on demande"
* generation of historic (academic transcript, ...)
* generation of assignment correction (see example below)

## Utilisation
To get the resulting '.tex' file, simply type the following command in your favorite terminal.
```bash
python3 main.py path/to/your/file.ptex
```
The '.tex' file will be located in the exact same directory that the '.ptex' file. (NB : a ```--output=<path>``` feature will be implemented)

## Example
```latex
\documentclass[a4paper,11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}

\begin{document}

<?
from random import randint

def reformat(string):
    return string[2:]

ex = [randint(0, 128) for i in range(25)]
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
Or alternatively,
```latex
\documentclass[a4paper,11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}

\begin{document}

<?
from random import randint
from utils.latex import Tabular

def reformat(string):
    return string[2:]

ex = [randint(0, 128) for i in range(25)]
res = [[str(e), reformat(bin(e)), reformat(hex(e))] for e in ex]
out("%"+str(ex))
?>

\section{Correction exercice 1}
\begin{center}
<?
tabular = Tabular(res)
tabular.setHeader(["dec", "bin", "hex"])
out(tabular)
?>
\end{center}

\end{document}
```
