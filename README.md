# count21ゲーム
ロボットシステム学の課題2で作成したものです。  
guiを用いたcount21ゲームをできるROSパッケージを作成しました。
## count21とは？
- ２１ゲームは１から順番に交互に数字を言い２１を言わされた方が負けて罰ゲームというシンプルなゲームです。
- ただし１度に言える数字は３つまでです。
### 例
- 先攻「１・２・３」
- 後攻「４・５」
- ・・・
- 先攻「19・20」
- 後攻「21」>> 負け
## 動作環境
以下の環境にて動作確認を行っています。  
  
- OS: Ubuntu 20.04.1 LTS
- ROs: Noetic
- python: 3.8.5

## 使い方
```bash
git clone https://github.com/masakifujiwara1/count21.git  
cd myled  
make  
sudo insmod myled.ko  
sudo chmod 666 /dev/myled0  
echo (0~3) > /dev/myled0
```
- pin番号22 : GPIO 25を使ってください。
- 使用した回路図  
![スクリーンショット 2020-11-29 175226](https://user-images.githubusercontent.com/72371743/100537400-a9683380-326b-11eb-9b56-2a43d93f53ac.png)

## 内容
- echo 0 の時：LED消灯
- echo 1 の時：LED点灯
- echo 2 の時:モールス信号のSOS（・・・ －－－ ・・・）を再現したLEDの点滅
<img src="https://user-images.githubusercontent.com/72371743/100539171-eafedb80-3277-11eb-8cd0-c2c7a193b4a7.gif"  width="500px">  

- echo 3 の時：LEDのpwm制御
<img src="https://user-images.githubusercontent.com/72371743/100539304-e38c0200-3278-11eb-998f-0fcd046b23b5.gif" width="500px">

  
## pwm制御について
- 4sかけてduty比が0%→100%→0%になるようになっています。
- 10msでduty比が0.5%増減→1sで50％ほど変化
## youtube
https://www.youtube.com/watch?v=1XYUYnG7E9o&ab_channel=%E5%8B%95%E7%94%BB%E4%BF%9D%E7%AE%A1%E5%BA%AB
## LICENSE
- [BSD 3-Clause License](https://github.com/masakifujiwara1/count21/blob/master/LICENSE)
## 参考
- https://qiita.com/hosizame/items/051a043f19e4955423f2
