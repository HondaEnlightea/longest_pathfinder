# 経路探索を行うクラス
class PathFinder:
    def __init__(self, graph):
        self.graph = graph
    
    #幅優先探索を用いて最短経路を求める関数
    def find_shortest_path(self, start, goal):
        
        # キュー(FIFO)を使って探索
        queue = []         # 経路をリストで保存
        queue.append([start])  
        visited = []      # 訪問済みの場所を記録、無限ループを防ぐ
        visited.append([start])

        while len(queue) > 0:
            path = queue.pop(0)  # 先頭の要素を取り出す
            current = path[-1]   # 現在地（経路の終端）
            
            # ゴールに到達したかの判定
            if current == goal:
                return path     #ゴールを含む経路を返す
            
            # 現在地に隣接する都道府県を全て調べる(幅方向を優先している)
            neighbors = self.graph.get_neighbors(current)
            for neighbor in neighbors:
                # まだ訪問していない場所のみ
                if neighbor not in visited:
                    visited.append(neighbor)
                    new_path = path + [neighbor]
                    queue.append(new_path)
        
        return None
    

    #指定した数以上の都道府県を通る経路を探す
    def find_best_efforts_path(self, start, goal, target_number):
        
        #見つかった経路の中で最長を保存
        longest_path = []  # 最長経路を保存するリスト
        
        #スタック(FILO)を使って探索(リスト形式)
        stack = []
        stack.append((start, [start]))
        
        path_count = 0  # 調べた経路の数
        
        while len(stack) > 0:
            current, path = stack.pop()
            path_count += 1
            
            # ゴールに到達したか確認
            if current == goal:
                
                # 一番長い経路を更新
                if len(path) > len(longest_path):
                    longest_path = path
                    path_edge = len(longest_path) - 1  # 通過した県数(スタート除く)(グラフ理論でいうところのエッジの本数)
                    print(f"さらに長い経路を発見: {path_edge}県通過")
                # 条件を満たしているかチェック
                    if path_edge >= target_number:
                        print(f"{path_count}本の経路を調査")   
                        print(f"条件達成。 {path_edge}県を通過する経路を発見")
                        return longest_path  # 条件を満たす経路を返す
            else:
                # 隣接する都道府県を探索(ゴールに到達しなかった場合)
                for neighbor in self.graph.get_neighbors(current):
                    # 既に通った場所は避ける
                    if neighbor not in path:
                        stack.append((neighbor, path + [neighbor]))

        # 条件を満たす経路が見つからなかった場合 
        path_edge = len(longest_path) - 1      
        print(f"探索終了。{path_count}本の経路を調査")
        print(f"条件を満たす経路は見つかりませんでした。\n {path_edge}県を通過する経路が最長経路です")
        return longest_path

#深さ優先探索で最長経路を求める関数
#これを改良し,目標通過数を満たす経路を見つけるようにしたのが前述の関数     
"""
 # 深さ優先探索を用いて最長経路を探索する関数
    def find_longest_path(self, start, goal):
        
        # 見つかった経路の中で最長のもの
        longest_path = []
        
        # スタック(FILO)を使って探索（リスト形式）
        stack = []
        stack.append((start, [start]))  # (現在地, 経路)のタプル形式で各要素を表現
        
        while len(stack) > 0:
            current, path = stack.pop()#最後の要素を取り出す
    
            # ゴールに到達したか確認
            if current == goal:
                # 最長経路を更新
                if len(path) > len(longest_path):
                    longest_path = path
            else:
                # 隣接する都道府県を探索(ゴールに到達しなかった場合)
                for neighbor in self.graph.get_neighbors(current):
                    # 既に通った場所は避ける
                    if neighbor not in path:
                        stack.append((neighbor, path + [neighbor]))
        
        return longest_path
"""