# separator
 Separator is designed to browse and classify pictures.

 It worked with Flask and React, before using you should put your image files into folder named origin.

## structure

```
 .
 ├── LICENSE
 ├── README.md
 ├── origin
 │   ├── your_files_here.bmp
 │   ├── your_files_here.bmp
 │   ├── your_files_here.bmp
 │   └── ...
 ├── separator.py
 └── static
     └── index.html
```

## dependencies

* Python 3.8.2 or whatever
* Flask

## instruction

1. Make a folder named `origin`, it has to be `origin`.
2. Install `Python` and `Flask`.
3. Open a terminal and input commands below.
```bash
$ export FLASK_APP=separator.py
$ flask run
```
4. Open browser with `http://127.0.0.1:5000/`
5. `j` for class j, `k` for class k, `space` for class space.
6. Your results will be remanaged into folder `j`,`k` and `space`.
