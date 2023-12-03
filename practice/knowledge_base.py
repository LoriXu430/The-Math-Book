import sqlite3

class KnowledgeBase:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_article(self, title, content):
        self.cursor.execute('INSERT INTO articles (title, content) VALUES (?, ?)', (title, content))
        self.conn.commit()

    def get_article(self, article_id):
        self.cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
        return self.cursor.fetchone()

    def update_article(self, article_id, title, content):
        self.cursor.execute('UPDATE articles SET title = ?, content = ? WHERE id = ?', (title, content, article_id))
        self.conn.commit()

    def delete_article(self, article_id):
        self.cursor.execute('DELETE FROM articles WHERE id = ?', (article_id,))
        self.conn.commit()

# Example usage
if __name__ == "__main__":
    kb = KnowledgeBase('knowledge_base.db')
    kb.add_article("Test Article", "This is a test article.")
