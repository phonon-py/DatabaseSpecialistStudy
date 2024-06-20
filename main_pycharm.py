from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import pandas as pd

# データベースエンジンの作成
engine = create_engine('sqlite:///example.db', echo=True)
metadata = MetaData()

# 既存のテーブルの読み込み
questions = Table('questions', metadata, autoload_with=engine)

# 新しいデータのインサート
new_data = [
    {
        'question': '新しい質問の例です。アクセス透過性を説明したものはどれか？',
        'choice_1': '選択肢1の説明。',
        'choice_2': '選択肢2の説明。',
        'choice_3': '選択肢3の説明。',
        'choice_4': '選択肢4の説明。',
        'answer': '選択肢1の説明。'
    },
    {
        'question': 'もう一つの質問の例です。アクセス透過性を説明したものはどれか？',
        'choice_1': '選択肢1の説明。',
        'choice_2': '選択肢2の説明。',
        'choice_3': '選択肢3の説明。',
        'choice_4': '選択肢4の説明。',
        'answer': '選択肢1の説明。'
    }
]

# データをインサート
with engine.begin() as conn:  # engine.begin()で自動コミットを行うトランザクションブロックを使用
    result = conn.execute(questions.insert(), new_data)
    print(f"Inserted {result.rowcount} rows")

# データの取得と確認
df = pd.read_sql(questions.select(), engine)
print(df)