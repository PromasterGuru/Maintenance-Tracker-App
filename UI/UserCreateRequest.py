+from flask_restplus import TestCase
+from flask_restplus.namespace import Namespace
+
+client = Namespace('users')
+
+
+class UsersCreateRequests(TestCase):
+    def getRequest(self):
+        pass
+
+    def postRequest(self):
+        pass