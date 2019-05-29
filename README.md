# 構築環境
Python 3.6.7  
Django 2.1.8  
SQLite 3.7.17  

# ローカル開発環境での実行
## リポジトリからソースコードを取得
$ git clone git@github.com:acecrc/django-todo.git  
$ cd django-todo  

## 仮想環境の構築
$ virtualenv ~/eb-virt  
$ source ~/eb-virt/bin/activate  
(eb-virt) $ pip3 install -r requirements.txt  

## マイグレーションの実施
(eb-virt) $ python3 manage.py migrate  

## アプリケーションの起動
(eb-virt) $ python3 manage.py runserver 8080  

## 動作確認
ブラウザでToDoの一覧を表示させる。  
http://127.0.0.1:8080/todo/list/  
