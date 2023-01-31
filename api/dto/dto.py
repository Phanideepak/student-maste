from flask_restx import Namespace,fields

class DepartmentDto:
    api = Namespace('department',description= 'Namespace for department apis')
    hod_details = api.model('hod_details',{
        'name' : fields.String(attribute = 'name', description = 'hod name', required=True),
        'email': fields.String(attribute = 'email', description = 'hod email', required=True),
        'phone' : fields.String(attribute = 'phone', description = 'hod contact', required=True) 
    })
    add_department_request = api.model('department',{
        'name': fields.String(attribute = 'name', description = 'department name', required=True),
        'description': fields.String(attribute = 'description', description = 'department description', required=True),
        'hod_details': fields.Nested(hod_details,required=True)        
    })
    update_department_request = api.model('department',{
        'department_id': fields.Integer(attribute = 'id', description = 'department id', required=True),
        'name': fields.String(attribute = 'name', description = 'department name', required=True),
        'description': fields.String(attribute = 'description', description = 'department description', required=True),
        'hod_details': fields.Nested(hod_details,required=True) 
    })

class StudentDto:
    api = Namespace('student', description ='Namespace for student apis')
    student = api.model('student',{
        'name': fields.String(attribute = 'name', description = 'student name',required=True)
    })
class DegreeDto:
    api = Namespace('degree', description='Namespace for degree apis')
    add_degree_request = api.model('degree',{
        'name': fields.String(attribute = 'name', description = 'degree name', required=True),
        'description': fields.String(attribute = 'description', description = 'degree description', required=True),
        'duration': fields.Integer(attribute = 'duration', description = 'duration', required=True),
        'single': fields.Boolean(attribute='single', description= 'single or dual degree', required=True)
    })

class UserDto:
    api = Namespace('auth', description ='Namespace for authentication')
    user_request_dto = api.model('user',{
        'id' : fields.Integer(),
        'username': fields.String(attribute = 'user_name', description = 'user name', required=True),
        'email': fields.String(attribute = 'email', description = 'user email id', required=True),
        'password': fields.String(attribute = 'pwd',description = 'user password', required = True),        
    })
    login_request_dto = api.model('user',{
        'email': fields.String(attribute = 'email', description = 'user email id', required=True),
        'password': fields.String(attribute = 'pwd',description = 'user password', required = True),
    })