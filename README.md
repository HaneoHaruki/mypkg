# 沖縄の温度・湿度publisher  
[![test](https://github.com/HaneoHaruki/robosyshomework2/actions/workflows/test.yml/badge.svg)](https://github.com/HaneoHaruki/robosyshomework2/actions/workflows/test.yml)  

## 概要  

このROS2パッケージは、現在の沖縄の気温と湿度の情報を表示できる機能があります。気温はTemperature、湿度はHumidityとして表示されます。

## 依存関係  

パッケージを動かすために必要なライブラリ
- `requests`:HTTPリクエストを処理するために必要
```
$ pip install requests
```

## 使用方法  
## 実行準備  

1.[openweathermap.org](https://openweathermap.org/)でアカウントを作成してAPIキーを取得して下さい。  
2.環境変数を設定:  
```
$ echo "export WEA_API_KEY='取得したAPIキー'" >> ~/.bashrc
$ source ~/.bashrc
```

## ノードを実行  
### weatherpublisher.pyの実行
```
$ ros2 run mypkg weatherpublisher  
```

### データの確認  
別の端末で以下を実行してトピックのデータを表示します。

```
$ ros2 topic echo weatherpublisher  
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
このパッケージは以下の環境で動作が確認済みです。
- **OS**: Ubuntu 22.04 LTS
- ROS2 humble

## ライセンス 

- このソフトウェアは 3条項BSDライセンス の下で再頒布および使用が許可されています。
- 詳細は[LISENCE](https://github.com/HaneoHaruki/mypkg/blob/main/LICENSE)を確認して下さい。
- ©2025 Haruki Haneo
