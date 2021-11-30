<h1>Zoom FrontRow Pipeline</h1>
An automation code to extract Zoom recording links from multiple Zoom accounts.
<h2>Requirements</h2>
<h3>Hardware</h3>

- 128GB SSD<br>
- 8GB RAM<br>
- Intel I5 Core Processor

<h3>Software</h3>

- Linux Operating System <br>
- Python 3.5+ <br>

<h2>Usage</h2>

- Place the file that contains the client details under `input` folder

- Rename the file to `clients.csv`

- Create a python virtual environment using the following command (cwd)
```
python3 -m venv zpvenv
```

- Install the requirements through the virtual environment (zpvenv)
```
zpvenv/bin/python3 -m pip install -r requirements.txt 

```

- Run the main script in the same virtual environment
```
zpvenv/bin/python3 main.py
```

- CSV files generated exist under the `bundle` folder in the same directory
