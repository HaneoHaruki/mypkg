# 沖縄の温度・湿度publisher  
[![test](https://github.com/HaneoHaruki/robosyshomework2/actions/workflows/test.yml/badge.svg)](https://github.com/HaneoHaruki/robosyshomework2/actions/workflows/test.yml)
##概要  

このROS2パッケージは、現在の沖縄の気温と湿度の情報を表示できる機能があります。気温はTemperature、湿度はHumidityとして表示されます。

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
data: 'Temperature: 16.57°C, Humidity: 96%'
---
data: 'Temperature: 16.57°C, Humidity: 96%'
---
data: 'Temperature: 16.57°C, Humidity: 96%'
---
data: 'Temperature: 16.57°C, Humidity: 96%'
---
data: 'Temperature: 19.35°C, Humidity: 80%'
---
data: 'Temperature: 16.57°C, Humidity: 96%'
---
```

## 動作環境

- **OS**: Ubuntu 22.04 LTS

## ライセンス 

- このソフトウェアは 3条項BSDライセンス の下で再頒布および使用が許可されています。

## Copyright  

- ©2025 Haruki Haneo
