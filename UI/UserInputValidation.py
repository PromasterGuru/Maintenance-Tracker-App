+from flask_restplus import TestCase
+from flask_restplus.namespace import Namespace
+
+client = Namespace('users')
+
+
+class UsersInputValidation(TestCase):
+    def get(self,user_input):
+        pass
+
+    def put(self,user_input):
+        pass