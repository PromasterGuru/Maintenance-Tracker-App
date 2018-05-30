+from flask_restplus import TestCase
+from flask_restplus.namespace import Namespace
+
+client = Namespace('users')
+
+
+class AdminFilterRequests(TestCase):
+    def getFilter(self,request_type):
+        pass
+
+    def putFilter(self,request_type):
+        pass