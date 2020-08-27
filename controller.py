import web
from models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/postregistration', 'PostRegistration',
    '/checklogin', 'CheckLogin',
    '/logout', 'Logout',
    '/postactivity', 'PostActivity',
    '/profile', 'Profile',

)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("views/Templates", base="MainLayout",
                             globals={'session': session_data, 'current_user': session_data['user']})


class Home:
    def GET(self):
        data = type("obj", (object,), {"username": "nit", "password": "12345"})

        login = LoginModel.LoginModel()
        iscorrect = login.check_user(data)

        if iscorrect:
            session_data['user'] = iscorrect

            post_model = Posts.Posts()
            posts = post_model.get_all_posts()

        return render.Home(posts)


class Register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data.username


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        iscorrect = login.check_user(data)

        if iscorrect:
            session_data["user"] = iscorrect
            return iscorrect

        return "error"


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"


class Profile:
    def GET(self):
        post_model = Posts.Posts()
        posts = post_model.get_all_posts()

        return render.Profile(posts)


if __name__ == "__main__":
    app.run()
