# count21ゲーム
ロボットシステム学の課題2で作成したものです。  
guiを用いてcount21ゲームをできるROSパッケージを作成しました。
## count21ゲームとは？
- count21ゲームは１から順番に交互に数字を言い２１を言わされた方が負けというシンプルなゲームです。
- ただし１度に言える数字は３つまでです。
- パスをした場合も負けです。
### 例
- 先攻「１・２・３」
- 後攻「４・５」
- ・・・
- 先攻「19・20」
- 後攻「21」>> 21を言わされたので後攻の負け
## 動作環境
以下の環境にて動作確認を行っています。  
  
- OS: Ubuntu 20.04.1 LTS
- ROS: Noetic
- python: 3.8.5


## インストール方法

### ソースからビルドする方法

- [ROS Wiki](http://wiki.ros.org/ja/kinetic/Installation/Ubuntu)を参照しROSをインストールします。

- `git`を使用して本パッケージをダウンロードします。

  ```bash
  cd ~/catkin_ws/src
  git clone https://github.com/masakifujiwara1/count21.git
  ```
- `catkin_make`を使用して本パッケージをビルドします。

  ```bash
  cd ~/catkin_ws && catkin_make
  source ~/catkin_ws/devel/setup.bash
  ```

## 実行
下記のコマンドを別々の端末で実行してください。
```bash
roscore
rosrun count21 cpu.py
rosrun count21 count21.py
```
上記のコマンドを実行したら、それ以降は出力される指示に従ってください。



<img src="https://user-images.githubusercontent.com/72371743/103683789-fdcea380-4fcd-11eb-81b3-faa364dbd27d.gif" width="500px">

  

## Youtube
https://www.youtube.com/watch?v=-DQhdrYhHj8
## LICENSE
[BSD 3-Clause License](https://github.com/masakifujiwara1/count21/blob/master/LICENSE)
## 参考
https://qiita.com/hosizame/items/051a043f19e4955423f2
