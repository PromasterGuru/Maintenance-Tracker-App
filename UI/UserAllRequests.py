+from flask_restplus import TestCase
+from flask_restplus.namespace import Namespace
+
+client = Namespace('users')
+
+
+class UserAllRequests(TestCase):
+    def get(self,user_id: int):
+        pass
+
+    def put(self,user_id: int):
+        pass