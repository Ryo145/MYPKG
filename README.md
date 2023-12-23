# mypkg
[![test](https://github.com/Ryo145/mypkg/actions/workflows/test1.yml/badge.svg)](https://github.com/Ryo145/mypkg/actions/workflows/test1.yml)

このリポジトリは千葉工業大学先進工学部未来ロボティクス学科４sのロボットシス>テム学の講義で使用したものである。

# インストール方法
ROS2を使用できる環境でこのリポジトリをクローンして使用する。  
以下でクローン出来る。

```
$ git clone https://github.com/Ryo145/mypkg.git
```

# ノード
## 1. talker1
   * 機能

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

   * 実行方法

   ```
   $ ros2 run mypkg listener3
   ```

   * 実行結果
   
   ```
   $ ros2 run mypkg listener3
   [INFO] [1703308284.649941438] [Listen3]: Listen3: 11.000000
   [INFO] [1703308285.132041240] [Listen3]: Listen3: -11.000000
   [INFO] [1703308285.628555035] [Listen3]: Listen3: 44.000000
   [INFO] [1703308286.128593126] [Listen3]: Listen3: -440.000000
   [INFO] [1703308286.632854762] [Listen3]: Listen3: 8800.000000
   [INFO] [1703308287.132970836] [Listen3]: Listen3: -308000.000000
   ```

## 5. listener4
   * 機能

   * 実行方法

   ```
   $ ros2 run mypkg listener4
   ```

   * 実行結果
   
   ```
   $ ros2 run mypkg listener4
   [INFO] [1703308284.656660605] [Listen4]: Listen4: 100000.000000
   [INFO] [1703308285.133894670] [Listen4]: Listen4: -1.000000
   [INFO] [1703308285.629185959] [Listen4]: Listen4: -0.250000
   [INFO] [1703308286.129319611] [Listen4]: Listen4: -0.100000
   [INFO] [1703308286.634834221] [Listen4]: Listen4: -0.050000
   [INFO] [1703308287.134960648] [Listen4]: Listen4: -0.028571
   ```
　
# ローンチ
   talker1,listener1,listener2,listener3,listener4を同時に実行することができる。
   * 実行方法
   
   ```
   $ ros2 launch mypkg t1_l1_l2_l3_l4.launch.py
   ```

   * 実行結果
   
   ```
   $ ros2 launch mypkg t1_l1_l2_l3_l4.launch.py
   [INFO] [launch]: All log files can be found below /home/bellsryo/.ros/log/2023-12-23-14-27-41-269560-localhost-1449
   [INFO] [launch]: Default logging verbosity is set to INFO
   [INFO] [talker1-1]: process started with pid [1450]
   [INFO] [listener1-2]: process started with pid [1452]
   [INFO] [listener2-3]: process started with pid [1454]
   [INFO] [listener3-4]: process started with pid [1456]
   [INFO] [listener4-5]: process started with pid [1458]
   [listener1-2] [INFO] [1703309262.048109123] [Listen1]: Listen1: 0.000000
   [listener2-3] [INFO] [1703309262.054266616] [Listen2]: Listen2: 0.000000
   [listener3-4] [INFO] [1703309262.060234463] [Listen3]: Listen3: 71.000000
   [listener4-5] [INFO] [1703309262.066367404] [Listen4]: Listen4: 100000.000000
   [listener1-2] [INFO] [1703309262.540945024] [Listen1]: Listen1: 1.000000
   [listener2-3] [INFO] [1703309262.541718865] [Listen2]: Listen2: -1.000000
   [listener3-4] [INFO] [1703309262.542519136] [Listen3]: Listen3: -71.000000
   [listener4-5] [INFO] [1703309262.543312364] [Listen4]: Listen4: -1.000000
   [listener1-2] [INFO] [1703309263.042626815] [Listen1]: Listen1: 3.000000
   [listener2-3] [INFO] [1703309263.044762601] [Listen2]: Listen2: -4.000000
   [listener3-4] [INFO] [1703309263.046814648] [Listen3]: Listen3: 284.000000
   [listener4-5] [INFO] [1703309263.048974997] [Listen4]: Listen4: -0.250000
   ```

# 必要なソフトウェア
* ROS2  
* Python
 
# テスト環境
* Ubuntu 22.04.2 LTS

# 著作権・ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます． 
* © 2023 Ryosuke Suzuki
