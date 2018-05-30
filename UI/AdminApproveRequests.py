+from flask_restplus import TestCase
+from flask_restplus.namespace import Namespace
+
+client = Namespace('users')
+
+
+class AdminResolveRequests(TestCase):
+    def get(self,user_id,request):
+        pass
+
+    def put(self,user_id,user_input):
+        pass
