+---------------------+
| Student Code Input | (C++/Python)
|                     |
+----------+----------+
           |
           v
+------------------+
| Intention Agent  | (Intent Recognition & Tool Calling)
| (System Prompt)  |
+-----+----+-------+
      |    |
      |    |----------------------------------+
      v    v                                  v
+-----+----+----+        +--------------------+        +--------------------+
| Diagnoser      | (RAG) | RAG Database        |        | Output Generator  |
| Agent          +------>| (Programming knowledge base, |------>| Agent              |
| (Context       |       | past user errors, rules)     |        |                    |
| Window < 1M)   |       +--------------------+        +----+---------------+
+-----+----+----+                                           |
      |    |                                                v
      |    |------------------------------------------------+
      v    v                                                |
+-----+----+-----+                                          |
| Questioner Agent| (Heuristic Debugging)                  |
| (Multi-turn    |                                          |
| Conversation)  |------------------------------------------+
+----------------+