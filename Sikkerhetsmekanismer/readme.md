### General
The "MiljøOppsett" folder contains documentation for how the Kubernetes environment was configured, how the different security mechanisms were implemented, and how the performance tests were executed.

During an initial test phase, Grafana was used to visualize resource usage in the Kubernetes cluster. The folder "MiljøOppsett" contains a setup guide, and the captured images are stored in the "GrafanaBilder" folder. These results were not used in the paper, or the bachelorer thesis.

### How to parse results from .txt to .csv
The script "parse.py" takes a single .txt file as input and converts it to .csv format.
To use custom files, the script must be edited so that the filename located at the bottom matches the .txt file you want to parse.

### How to use the plotting scripts
The scripts "linjediagram.py", "søylediagram.py" og "tabell.py" take 5 csv files, one for each of the tests, and generates line charts, bar charts and tables with percentage deviation, respectively.
To use custom files, you must edit the script so the filenames, defined at the top, matches you .csv files and change the labels accordingly.
