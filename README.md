# 沖縄の温度・湿度publisher  

このROS2パッケージは、現在の沖縄の気温と湿度の情報を表示できる機能があります。  

## ノードの概要  
### weatherpublisherノード  
- トピック名: 'weatherpublisher'  

- 1秒ごとに以下のように情報を出力します:  
```
気温: XX.X℃  湿度: YY.Y%  
```
- OpenWeatherMapサイトから沖縄の現在の気温と湿度を読み取り、それを表示します。  

## 使用方法  

### 必要条件 ###  
- ROS2をダウンロードします。  

### パッケージのセットアップ  

1.パッケージをクローンします。  
```
cd ~/ros2_ws/src  
```
```
git clone https://github.com/HaneoHaruki/robosyshomework2.git  
```

2.ビルドします。  
```
cd ~/ros2_ws  
```
```
colcon build  
```

3.ワークスペースをソース  
```
source ~/ros2_ws/install/setup.bash  
```

## ノードを実行  
### 実行コマンド  
### 送り手  
```
ros2 run mypkg weatherpublisher  
```
### 受け取り手  
```
ros2 topic echo weatherpublisher  
```

## 実行例  
### 送り手の実行例  
```
[INFO] [1736017821.465978037] [weather_publisher]: Published: 気温: 16.45°C, 湿度: 60%
[INFO] [1736017822.445411227] [weather_publisher]: Published: 気温: 16.45°C, 湿度: 60%
[INFO] [1736017823.441732505] [weather_publisher]: Published: 気温: 16.45°C, 湿度: 60%
[INFO] [1736017824.465051694] [weather_publisher]: Published: 気温: 16.45°C, 湿度: 60%
[INFO] [1736017825.497072051] [weather_publisher]: Published: 気温: 15.85°C, 湿度: 64%
```

### 受け取り手の実行例  
```
data: '気温: 16.45°C, 湿度: 60%'
---
data: '気温: 16.45°C, 湿度: 60%'
---
data: '気温: 16.45°C, 湿度: 60%'
---
data: '気温: 16.45°C, 湿度: 60%'
---
data: '気温: 15.85°C, 湿度: 64%'
---
```

## 動作環境

このパッケージは以下の環境で動作が確認済み:
- **OS**: Ubuntu 20.04 LTS
- **Python**
  - テスト済みバージョン3.10

## ライセンス
- このソフトウェアは 3条項BSDライセンス の下で再頒布および使用が許可されています。
-  このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを本人の許可を得て自身の著作としたものです。
    - [ryuichiueda/slides_marp/tree/master/robosys_2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- このパッケージのテストに利用したコンテナは下記のリンクのものを、本人の許可を得て使用しています
  - [ryuichiueda/ubuntu22.04-ros2:latest](https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2)
- ©2025 Haruki Haneo
