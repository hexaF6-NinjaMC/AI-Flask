from flask import request, abort, render_template
from flask_admin import AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from datetime import datetime

class MyModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.id == 1:
            return True
        return False
    
    def inaccessible_callback(self, name, **kwargs):
        with open('app/static/assets/logs/http-errors.txt', 'a+') as error_file:
            error_file.writelines(f'Timestamp: {datetime.utcnow()}\n\t"403: Trying to access a Model in {request.path} - {request.remote_addr}"\n\n'), abort(404)
    
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.id == 1:
            return True
        return False
    
    def inaccessible_callback(self, name, **kwargs):
        with open('app/static/assets/logs/http-errors.txt', 'a+') as error_file:
            error_file.writelines(f'Timestamp: {datetime.utcnow()}\n\t"403: Trying to access AdminIndex in {request.path} - {request.remote_addr}"\n\n'), abort(404)

class GoHomeView(BaseView):
    @expose('/')
    def go_home(self):
        """
            Adds a link that sends the admin user back to blog home page from admin section
        """
        return render_template('index.html')