from flet import *

def main(page: Page):
    page.__dark_theme=True
    page.title = 'Hossam Sallam'
    page.bgcolor = colors.BLACK
    page.window.title_bar_hidden = False
    page.window.width = 390
    page.window.height = 740

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(
                    ),
                    Row([
                            Image(src="photo.gif"),
                        ], alignment=MainAxisAlignment.CENTER,
                        height=200
                        ),
                        #toolbar_height=200,
                
                    Row([Text("....مرحبا في استثماري", size=24, color="BLACK", width=370, text_align="center")],alignment=MainAxisAlignment.CENTER),
                    Container(height=200),
                    Row([
                        ElevatedButton("تسجيل دخول", width=170, style=ButtonStyle(bgcolor='BLUE', color='white'), on_click=lambda _: page_go("/login")),
                        ElevatedButton("حساب جديد", width=170, style=ButtonStyle(bgcolor='BLUE', color='white'), on_click=lambda _: page_go("/signup")),
                    ], alignment=MainAxisAlignment.CENTER)
                ]
            )
        )
################### login page ####################################################
        if page.route == "/login":
            page.views.append(
                View(
                    "/login",
                    [
                        AppBar(
                            bgcolor="BLUE",
                            title=Text("Login system")
                        ),
                        Row([
                            Image(src="photo.gif"),
                        ], alignment=MainAxisAlignment.CENTER,
                        height=200
                        ),
                     Row([Text("تسجيل الدخول", size=24, color="BLACK",width=370, text_align='center'),],alignment=MainAxisAlignment.CENTER
                         ),
                    TextField(label='Email : ادخل البريد الالكتروني',icon=Icons.EMAIL_SHARP),
                    TextField(label=' password : كلمه المرور',password=True,icon=icons.PASSWORD_SHARP),
                    Row([
                        ElevatedButton(" دخول", width=170, style=ButtonStyle(bgcolor='BLUE', color='white'), on_click=lambda _: page_go("/login")),
                        ElevatedButton("حساب جديد", width=170, style=ButtonStyle(bgcolor='BLUE', color='white'), on_click=lambda _: page_go("/signup")),
                    ], alignment=MainAxisAlignment.CENTER)
                    ]
                )
            )
################### sigup page ####################################################
        if page.route == "/signup":
            page.views.append(
                View(
                    "/signup",
                    [
                        AppBar(
                            bgcolor="BLUE",
                            title=Text("Signup Page")
                        ),
                    Row([
                            Image(src="photo.gif"),
                        ], alignment=MainAxisAlignment.CENTER,
                        height=200
                        ),
                    Row([Text(" انشاء حساب جديد", size=24, color="BLACK",width=370, text_align='center')],alignment=MainAxisAlignment.CENTER),
                    TextField(label='Email : ادخل البريد الالكتروني'),
                    TextField(label='Name :  الاسم بالكامل'),
                    TextField(label='Num Phone :  رقم الهاتف'),
                    TextField(label='password : كلمه المرور',password=True),
                    TextField(label='password : تاكيد كلمه المرور',password=True),
                    Row([
                        ElevatedButton(" انشاء حساب ", width=170, style=ButtonStyle(bgcolor='BLUE', color='white'), on_click=lambda _: page_go("/sigup")),
                        ElevatedButton(" لديك حساب ", width=170, style=ButtonStyle(bgcolor='BLUE', color='white'), on_click=lambda _: page_go("/login")),
                    ], alignment=MainAxisAlignment.CENTER)
                    ]
                )
            )

            ########################home#################################333
            page.views.append(
                "/home",
                
            )

        page.update()

    def page_go(route):
        page.go(route)

    page.on_route_change = route_change
    page.on_view_pop = page_go
    page.go(page.route)

app(main)
