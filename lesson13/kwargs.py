def create_person(**kwargs):
    print(kwargs)
    return kwargs

create_person(name="Jim", occupation="teacher")
create_person(name="Bruce", ability="fly")