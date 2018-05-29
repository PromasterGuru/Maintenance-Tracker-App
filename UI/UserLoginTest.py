class UserLoginTest(TestCase):
    def setUp(self):
        self.client = User()

    def test_administration_login(self):
        response = self.client.get(
            reverse('user:index'),
            follow=True
        )
        self.assertEquals(response.status_code, 200)

        title = "User Login Title"
        self.assertTrue(title in response.content)

        user = User.objects.create(
            username='username', password=password('password')
        )
        self.assertTrue(user)

        is_logged_in = self.client.login(username='username', password="password")
        self.assertTrue(is_logged_in)

        response = self.client.post(
            reverse('user:index')
        )
        self.assertEqual(response.status_code, 302)

        self.assertRedirects(
            response,
            expected_url=reverse('user:user_dashboard'),
            status_code=302,
            target_status_code=200
        )