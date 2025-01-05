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

1.ビルドします。  
```
cd ~/ros2_ws  
```
```
colcon build  
```

2.ワークスペースをソース  
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

### 実行例  
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

- **OS**: Ubuntu 20.04 LTS

## ライセンス 

- このソフトウェアは 3条項BSDライセンス の下で再頒布および使用が許可されています。

## Copyright  
- ©2025 Haruki Haneo
