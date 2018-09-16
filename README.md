# gtrans
google translate command

## how to install
```
pip install https://github.com/umaumax/gtrans/archive/master.tar.gz
```

## how to use
```
gtrans cat
echo 'cat' | gtrans
gtrans # send clipboard
```

## NOTE
* supports proxy

----

## this is also repository of pip package sample
```
$ tree .
├── README.md
├── gtrans
│   ├── __init__.py
│   └── gtrans.py
├── requirements.txt
└── setup.py

1 directory, 5 files
```

* 最低限必要なもの
  * `__init__.py`: コマンドとして配布するときにも必要(空ファイルでも問題ない)

### ライブラリとして配布
* WIP

### コマンドとして配布
setup.py の 関数 setup の中に entry_points を加えることで、そのモジュールをコマンドとしてインストールできます。

> setup.py の 関数 setup の中に entry_points を加えることで、そのモジュールをコマンドとしてインストールできます。

### packageの試し方
#### install(update)
```
pip install .
```

#### check package
```
pip freeze
```

#### uninstall
```
pip uninstall $package_name
```
