#policy.py

def get():
    print('from policy.py')


# from glance.api import versions
# versions.create_resource('a.conf')

# from glance.db import models
# models.register_models('mysql')






#
if __name__ == '__main__':

    import versions
    versions.create_resource('a.conf')

else:
    from ..db import models
    models.register_models('mysql')