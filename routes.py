from resource import (

    EmployeeListResource,

    EmployeeResource
)

def initialize_routes(api):

    api.add_resource(

        EmployeeListResource,

        "/employees"
    )

    api.add_resource(

        EmployeeResource,

        "/employees/<int:id>"
    )