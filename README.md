# gtrans
google translate command

~~* FYI: [python \- Why "Googletrans\.Translator" suddenly stopped working? \- Stack Overflow]( https://stackoverflow.com/questions/52446811/why-googletrans-translator-suddenly-stopped-working )~~

## how to install
```
# for avoiding 'pip Installing collected packages: UNKNOWN'
pip install setuptools --upgrade
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
----
----
----

## This is also repository of pip package sample for me
* 基本的な構成
```
$ tree .
├── README.md
├── entry_points.cfg
├── gtrans
│   ├── __init__.py
│   └── gtrans.py
├── setup.cfg
└── setup.py

1 directory, 6 files
```

* `__init__.py`: ライブラリとしてはもちろんコマンドとして配布するときにも必ず必要(空ファイルでも問題ない)

### 最近の方法
* [setuptools: Pythonパッケージ作成 \- Heavy Watal]( https://heavywatal.github.io/python/setuptools.html )
* [Building and Distributing Packages with Setuptools — setuptools 40\.2\.0 documentation]( https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files )

#### memo
* コマンドとして配布する場合には
  * new:`setup.cfg`から`entry_points.cfg`を読み込むようにする
  * old:(setup.py の 関数 setup の中に entry_points を加える)

### how to do trial and error
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
