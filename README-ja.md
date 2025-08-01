from pgsn import prettifyfrom pgsn import prettify

# PGSN: Programmable Goal Structuring Notation

アシュアランスケース生成のための関数型プログラミング環境

[![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## PGSNとは？

**PGSN** は、**Goal Structuring Notation (GSN)** に基づいて構造化されたアシュアランスケースを構築・変換するための、関数型プログラミング言語および実行環境です。従来のGSNが静的な図表を中心とするのに対し、PGSNは関数型およびオブジェクト指向の構文を用いて、GSN要素を動的かつ構造的に生成できます。

PGSNは現在、**Pythonに埋め込まれたDSL（ドメイン特化言語）**として実装されていますが、今後は独立した実装も計画されています。

---

## 特長

- **関数型プログラミングによるGSN記述**：アシュアランスケースを関数として記述
- **構成的・再利用可能**：GSN構造を柔軟に組み立て可能
- **オブジェクト指向サポート**：クラス／継承によるノード定義の拡張
- **セキュアな評価**：PGSNの評価はリソース制限付きのインタプリタで行われ、第三者コードの安全な実行を保証

---

## インストール

### Conda を使う場合

```bash
git clone https://github.com/yoriyuki/PGSN.git
cd PGSN
conda env create -f environment.yml -n PGSN
```

### pip を使う場合

```bash
git clone https://github.com/yoriyuki/PGSN.git
cd PGSN
pip install -r requirements.txt
```

---

## 基本例

```python
from pprint import pprint

from pgsn import *

g = goal(
    description="System is secure",
    support=strategy(
        description="Break into sub-goals",
        sub_goals=[
            goal(description="Input validated",
                 support=evidence(description="Static analysis passed")),
            goal(description="Output sanitized",
                 support=evidence(description="Fuzzing test succeeded"))
        ]
    )
)

pprint(prettify(g.fully_eval()))
```

```shell
% python -m examples.gsn
{'assumptions': [],
 'contexts': [],
 'description': 'System is secure',
 'gsn_type': 'Goal',
 'support': {'description': 'Break into sub-goals',
             'gsn_type': 'Strategy',
             'sub_goals': [{'assumptions': [],
                            'contexts': [],
                            'description': 'Input validated',
                            'gsn_type': 'Goal',
                            'support': {'description': 'Static analysis passed',
                                        'gsn_type': 'Evidence'}},
                           {'assumptions': [],
                            'contexts': [],
                            'description': 'Output sanitized',
                            'gsn_type': 'Goal',
                            'support': {'description': 'Fuzzing test succeeded',
                                        'gsn_type': 'Evidence'}}]}}
```

---

## 応用例

### 例1：テンプレートによる再利用

同じ説明文を持つ goal + evidence の構造を生成する再利用可能な関数を定義します。

```python
from pprint import pprint

from pgsn import prettify
from pgsn.stdlib import *
from pgsn.gsn_term import goal, evidence, strategy

# goal + evidence のテンプレート関数を定義
mk_goal_with_evidence = lambda_abs_keywords(
    {"desc": variable("desc")},
    goal(
        description=variable("desc"),
        support=evidence(description=variable("desc"))
    )
)

# テンプレートを適用してゴールを生成
g1 = mk_goal_with_evidence(desc="No hardcoded passwords")
g2 = mk_goal_with_evidence(desc="Input sanitized")
g3 = mk_goal_with_evidence(desc="Logging enabled")

# トップレベルのゴールに統合
top = goal(
    description="System is secure",
    support=strategy(
        description="Apply security principles",
        sub_goals=[g1, g2, g3]
    )
)

pprint(prettify(top.fully_eval()))
```

---

### 例2：`map_term` を用いた一括生成

複数の要件から自動的に goal + evidence の構造を生成します。

```python
from pprint import pprint

from pgsn.gsn_term import *

requirements = ["Firewall enabled", "Encrypted communication", "Access control active"]

goal_template = lambda_abs(variable("desc"),
    goal(description=variable("desc"),
         support=evidence(description=variable("desc")))
)

goals = map_term(goal_template, requirements)

secure_goal = goal(
    description="Security requirements fulfilled",
    support=immediate(goals)
)

pprint(prettify(secure_goal.fully_eval()))
```

---

### 例3：オブジェクト指向によるノード拡張

GSNの各要素はクラスです。継承により拡張が可能です。

```python
from pprint import pprint

from pgsn import *

# Goal を拡張するクラスを定義
CustomGoal = define_class("CustomGoal", goal_class, project="Alpha")

# クラスからインスタンス生成
g = instantiate(CustomGoal, description="Secure connection established",
    support=evidence(description="Verified by audit"))

pprint(prettify(g.fully_eval()))
```

---

## 技法と応用のまとめ

| 目的              | 使用技法                              |
|-------------------|-----------------------------------------|
| テンプレートの再利用 | ラムダ抽象とキーワード引数の定義              |
| 構造の一括生成       | `map_term` を用いたリスト展開                  |
| メタデータの付加     | クラス定義と `instantiate` による構成           |

---

## よく使う関数一覧

| 関数                         | 説明                                           |
|----------------------------|------------------------------------------------|
| `goal(...)`                | GSNのゴール（主張）を定義                     |
| `strategy(...)`            | ゴールを裏付ける推論戦略を記述                |
| `evidence(...)`            | ゴールを支える情報を記述                      |
| `context(...)`             | ゴールや戦略に対する文脈情報を追加            |
| `assumption(...)`          | 前提条件を明示                                |
| `immediate(...)`           | サブゴールを直接接続                          |
| `map_term(...)`            | リストに対して関数適用を行い複数ノード生成    |
| `lambda_abs(...)`          | 引数付きのラムダ抽象（位置引数）              |
| `lambda_abs_keywords(...)` | 引数付きのラムダ抽象（キーワード引数）        |
| `define_class(...)`        | GSNノードの再利用可能なクラスを定義           |
| `instantiate(...)`         | クラスからオブジェクト（GSNノード）を生成     |

---

## アーキテクチャ

| レイヤー     | コンポーネント                    | 概要                                     |
|--------------|-----------------------------------|------------------------------------------|
| コア         | `pgsn_term.py`                    | ラムダ計算に基づくインタプリタ              |
| DSL層        | `stdlib.py`, `gsn_term.py`        | GSN構成要素を定義するためのAPI群           |
| OO層         | `object_term.py`                  | クラス・継承を用いたノード型の再利用と拡張 |

---

## ライセンス

MITライセンス – 詳細は [LICENSE](LICENSE) をご覧ください。

© 国立研究開発法人産業技術総合研究所 (AIST) 2023–2024  
山形頼之 2025
```
