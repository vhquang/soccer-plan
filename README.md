# Requirement

Python > 3.5
For development, install the `requirements.txt`, preferably with pip:

```bash
pip install -r requirements.txt
```

# Run

To run the app, the `PYTHONPATH` need to be set to the root folder (`/`)
```bash
export PYTHONPATH=[path_to_the_repo]
python main.py
```

# Testing

Testing is done with [pytest](https://docs.pytest.org/en/latest/getting-started.html)
The test suite is located in `tests` folder.

Because running `> pytest` may not work Mac, to run the test more consistent on different platforms, use:
```bash
python -m pytest
```


For more information about `tkinter`:
http://effbot.org/tkinterbook/canvas.htm
http://www.tkdocs.com/tutorial/canvas.html
