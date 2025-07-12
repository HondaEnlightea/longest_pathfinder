from prefecture_graph import PrefectureGraph
from path_finder import PathFinder
import time

print("新潟県からの最長経路探索プログラム")

#グラフと探索クラスを用意
graph = PrefectureGraph()
finder = PathFinder(graph)

#目的地の入力
goal = input("目的地の都道府県名を入力してください: ")
#エラー処理
if not graph.is_valid(goal):
    print("エラー：正しい都道府県名を入力してください")
    exit()

#目標通過数の入力
try:
    target_number = int(input("\n目標とする経路長を入力してください\nこの値を超えるように探索を繰り返します: "))
    if target_number < 1:
        print("エラー：目標通過数は1以上である必要があります")
        exit()
except ValueError:
    print("エラー：有効な整数を入力してください")
    exit()

#新潟県から目的地への条件付き最長経路を探索
print(f"\n新潟県から{goal}までの経路の探索を開始")

#最短経路の探索
shortest = finder.find_shortest_path('新潟県', goal)
shortest_edge = len(shortest) - 1
print(f"\n参考：最短経路長は{shortest_edge}県")
if shortest_edge > target_number:
    print(f"目標経路長の{target_number}県は最短経路長を下回っています。")
    print(f"\n最短経路:\n{' -> '.join(shortest)}")
    print("終了")
    exit()

#最長経路の探索
start_time = time.time()

longest = finder.find_best_efforts_path('新潟県', goal, target_number)

end_time = time.time()
elapsed_time = end_time - start_time

#結果を出力
"""悩んだ点
    出力の一部は別のファイル内に記述している。(path_finder.py)
    欠点として可読性の低下が考えられるが、
    結果の出力を全てメインプログラムが担う場合、
    返り値以外の情報をメインプログラムが受け取る必要があり、
    そのような記述を最小限に抑えるためこのような構成にした。
"""
print(f"経路:\n {' -> '.join(longest)}")
print(f"探索時間:{elapsed_time:.2f}秒")
print(f"終了")
