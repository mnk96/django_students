from django.db import connection


def get_username(request):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT
                       users.surname, users.name, users.middle_name
                       from users_login, users, auth_user
                       WHERE users_login.id_login=auth_user.id
                       AND users_login.id_user=users.id
                       AND auth_user.username='{request.user}'""")
        row = cursor.fetchone()
        username = row[0] + ' ' + row[1] + ' ' + row[2]
        return username


def get_menu(request):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT
                       users.role_id from users_login, users, auth_user
                       WHERE users_login.id_login=auth_user.id
                       AND users_login.id_user=users.id
                       AND auth_user.username='{request.user}'""")
        row = cursor.fetchone()
        cursor.execute(f"""SELECT menu.item, menu.slug from menu, menu_roles
                       WHERE menu_roles.id_role={row[0]}
                       AND menu_roles.id_menu=menu.id""")
        row = cursor.fetchall()
        menu_item = {}
        for i in range(len(row)):
            key = row[i][0]
            item = 'menu:' + row[i][1]
            menu_item[key] = item
        return menu_item


def get_about_user(request):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT
                       users.text from users_login, users, auth_user
                       WHERE users_login.id_login=auth_user.id
                       AND users_login.id_user=users.id
                       AND auth_user.username='{request.user}'""")
        row = cursor.fetchone()
        return row[0]


def get_sum_salary(request):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT
                       users.salary from users_login, users, auth_user
                       WHERE users_login.id_login=auth_user.id
                       AND users_login.id_user=users.id
                       AND auth_user.username='{request.user}'""")
        row = cursor.fetchone()
        return row[0]


def get_sum_scholarship(request):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT
                       users.scholarship from users_login, users, auth_user
                       WHERE users_login.id_login=auth_user.id
                       AND users_login.id_user=users.id
                       AND auth_user.username='{request.user}'""")
        row = cursor.fetchone()
        return row[0]
