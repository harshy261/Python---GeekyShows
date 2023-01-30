# MYFILE MODULE



# # SYNTAX 1 ---->
# import Admin.service
# Admin.service.admin_service()

# import Admin.product
# Admin.product.admin_product()

# import Admin.Common.header
# Admin.Common.header.admin_common_header()

# import Admin.Common.footer
# Admin.Common.footer.admin_common_footer()





# # SYNTAX 2 ---->
# from Admin import service
# service.admin_service()

# from Admin import product
# product.admin_product()

# from Admin.Common import header
# header.admin_common_header()

# from Admin.Common import footer
# footer.admin_common_footer()





# # SYNTAX 3 ---->
# from Admin.service import admin_service
# admin_service()

# from Admin.product import admin_product
# admin_product()

# from Admin.Common.header import admin_common_header
# admin_common_header()

# from Admin.Common.footer import admin_common_footer
# admin_common_footer()

# from User.profile import user_profile
# user_profile()






# SYNTAX 4 ---->
from Admin import *
# service.admin_service()           # SHOWS ERROR 
# product.admin_service()           # SHOWS ERROR

# Make changes in __init__ file of Admin Package

service.admin_service() 
service.admin_service()            




