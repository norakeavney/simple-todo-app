import unittest
import os
import json
from todo import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.filename = "test_todos.json"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_and_load_todos(self):
        todo_list = TodoList(self.filename)
        todo_list.add_todo("Test task")

        new_todo_list = TodoList(self.filename)
        self.assertEqual(len(new_todo_list.todos), 1)
        self.assertEqual(new_todo_list.todos[0]['task'], "Test task")

    def test_load_from_nonexistent_file(self):
        todo_list = TodoList("nonexistent.json")
        self.assertEqual(todo_list.todos, [])

    def test_load_from_invalid_json_file(self):
        with open(self.filename, 'w') as f:
            f.write("invalid json")

        todo_list = TodoList(self.filename)
        self.assertEqual(todo_list.todos, [])

if __name__ == '__main__':
    unittest.main()
