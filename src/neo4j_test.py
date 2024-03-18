from neo4j import GraphDatabase
from functools import wraps
import ast

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
        
    # クエリを実行する
    def query_execute(self, query, message="default"):
        with self.driver.session() as session:
            session.run(query)
    
    # クエリを実行して結果を返す
    def execute_query_and_return_string(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            result_list = result.data()
            result_string = str(result_list[0]) if result_list else "No result"
            return ast.literal_eval(result_string) if result_string != "No result" else {}
    
    # 既存のデータを全削除する
    def clear_db(self):
        with self.driver.session() as session:
            session.run('MATCH (n) DETACH DELETE n')

# デコレータで省略する
def with_neo4j_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        greeter = HelloWorldExample("bolt://my_neo4j:7687", "neo4j", "password")
        try:
            return func(greeter, *args, **kwargs)
        finally:
            greeter.close()
    return wrapper