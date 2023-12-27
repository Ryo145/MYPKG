# mypkg  
[![test](https://github.com/Ryo145/mypkg/actions/workflows/test1.yml/badge.svg)](https://github.com/Ryo145/mypkg/actions/workflows/test1.yml)

このリポジトリは千葉工業大学先進工学部未来ロボティクス学科4sのロボットシステム学の講義で使用したものである。  

このリポジトリはROS2のパッケージです。

# インストール方法
ROS2を使用できる環境でこのリポジトリをクローンして使用する。  
以下でクローン出来る。

```
$ git clone https://github.com/Ryo145/mypkg.git
```

# ノード

以下のノードをすべて実行するにはターミナルが５つ必要です。  
メッセージの型はFloat64。

## トピックの説明

### /countup  
   トピック/countupは、0.5秒ごとに１から1ずつ増やしていく。
   
### /addition  
   トピック/additionは、受け取った数値を累計に加算していく。

### /subtraction  
   トピック/subtractionは、受け取った数値を累計から減算していく。

### /multiplication
   トピック/multiplicationは、受け取った値を累計に乗算していく。
   
## 1. talker1
   * 機能  
   数字をカウントして、トピック/countupを通じてメッセージを送信するパブリッシャを持つノードです。
   * 実行方法
   
   ```
   $ ros2 run mypkg talker1
   ```
   
   * 実行結果

   ```
   $ ros2 run mypkg talker1
   (なにも表示されないです)
   ```

## 2. listener1
   * 機能  
   トピック/countupからメッセージを受け取り、それを累計して、その合計をトピック/additionを通じてメッセージを送信するパブリッシャを持つノードです。
   * 実行方法

   ```
   $ ros2 run mypkg listener1
   ```

   * 実行結果
   
   ```
   $ ros2 run mypkg listener1
   [INFO] [1703308284.632429156] [Listen1]: Listen1: 0.000000
   [INFO] [1703308285.128334337] [Listen1]: Listen1: 1.000000
   [INFO] [1703308285.626982775] [Listen1]: Listen1: 3.000000
   [INFO] [1703308286.127089937] [Listen1]: Listen1: 6.000000
   [INFO] [1703308286.628852987] [Listen1]: Listen1: 10.000000
   [INFO] [1703308287.129080862] [Listen1]: Listen1: 15.000000
   ```

## 3. listener2
   * 機能  
   トピック/additionからメッセージを受け取り、それを累計から減算してその結果をトピック/subtractionを通じてメッセージを送信するパブリッシャを持つノードです。
   * 実行方法

   ```
   $ ros2 run mypkg listener2
   ```

   * 実行結果
   
   ```
   $ ros2 run mypkg listener2
   [INFO] [1703308284.643526101] [Listen2]: Listen2: 0.000000
   [INFO] [1703308285.130173364] [Listen2]: Listen2: -1.000000
   [INFO] [1703308285.627704779] [Listen2]: Listen2: -4.000000
   [INFO] [1703308286.127778382] [Listen2]: Listen2: -10.000000
   [INFO] [1703308286.630709042] [Listen2]: Listen2: -20.000000
   [INFO] [1703308287.131142173] [Listen2]: Listen2: -35.000000
   ```

## 4. listener3
   * 機能  
   トピック/subtractionからメッセージを受け取り、それを累計にかけ合わせその結果をトピック/multiplicationを通じてメッセージを送信するパブリッシャを持つノードです。
   * 実行方法

   ```
   $ ros2 run mypkg listener3
   ```

   * 実行結果
   
   ```
   $ ros2 run mypkg listener3
   [INFO] [1703410284.417474945] [Listen3]: Listen3: 91.000000
   [INFO] [1703410284.895044766] [Listen3]: Listen3: -91.000000
   [INFO] [1703410285.391837088] [Listen3]: Listen3: 364.000000
   [INFO] [1703410285.891745412] [Listen3]: Listen3: -3640.000000
   [INFO] [1703410286.391849436] [Listen3]: Listen3: 72800.000000
   [INFO] [1703410286.891915411] [Listen3]: Listen3: -2548000.000000
   ```

## 5. listener4
   * 機能  
   トピック/multiplicationからメッセージを受け取り、それを前回の値で割った値で計算しその結果を表示するサブスクライバを持つノードです。
   * 実行方法

   ```
   $ ros2 run mypkg listener4
   ```

   * 実行結果
   
   ```
   $ ros2 run mypkg listener4
   [INFO] [1703410284.424351306] [Listen4]: Listen4: 100000.000000
   [INFO] [1703410284.896841984] [Listen4]: Listen4: -1.000000
   [INFO] [1703410285.392625951] [Listen4]: Listen4: -0.250000
   [INFO] [1703410285.892539689] [Listen4]: Listen4: -0.100000
   [INFO] [1703410286.392583073] [Listen4]: Listen4: -0.050000
   [INFO] [1703410286.892763109] [Listen4]: Listen4: -0.028571
   ```
　
# ローンチ
   上記の五つのノードを同時に実行することができます。
   * 実行方法
   
   ```
   $ ros2 launch mypkg t1_l1_l2_l3_l4.launch.py
   ```

   * 実行結果
   
   ```
   $ ros2 launch mypkg t1_l1_l2_l3_l4.launch.py
   [INFO] [launch]: All log files can be found below /home/bellsryo/.ros/log/2023-12-24-18-35-15-198792-localhost-1413
   [INFO] [launch]: Default logging verbosity is set to INFO
   [INFO] [talker1-1]: process started with pid [1414]
   [INFO] [listener1-2]: process started with pid [1416]
   [INFO] [listener2-3]: process started with pid [1418]
   [INFO] [listener3-4]: process started with pid [1420]
   [INFO] [listener4-5]: process started with pid [1422]
   [listener1-2] [INFO] [1703410515.974966888] [Listen1]: Listen1: 0.000000
   [listener2-3] [INFO] [1703410515.981011344] [Listen2]: Listen2: 0.000000
   [listener3-4] [INFO] [1703410515.987055048] [Listen3]: Listen3: 28.000000
   [listener4-5] [INFO] [1703410515.993237744] [Listen4]: Listen4: 100000.000000
   [listener1-2] [INFO] [1703410516.467815095] [Listen1]: Listen1: 1.000000
   [listener2-3] [INFO] [1703410516.468683768] [Listen2]: Listen2: -1.000000
   [listener3-4] [INFO] [1703410516.469556114] [Listen3]: Listen3: -28.000000
   [listener4-5] [INFO] [1703410516.470309059] [Listen4]: Listen4: -1.000000
   [listener1-2] [INFO] [1703410516.967834754] [Listen1]: Listen1: 3.000000
   [listener2-3] [INFO] [1703410516.968647603] [Listen2]: Listen2: -4.000000
   [listener3-4] [INFO] [1703410516.969469447] [Listen3]: Listen3: 112.000000
   [listener4-5] [INFO] [1703410516.970188746] [Listen4]: Listen4: -0.250000
   ```

# 必要なソフトウェア
* ROS2  
* Python
 
# テスト環境
* Ubuntu 22.04.2 LTS

# 著作権・ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます． 
* © 2023 Ryosuke Suzuki
