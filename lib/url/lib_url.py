BASE_URL = 'https://app.remonline.ru'
DEV_URL = 'https://dev.remonline.ru'
NEXT_URL = 'https://next.remonline.ru'
STAGE_URL = 'https://stage.remonline.ru'

# Login & Registration
LOGIN_URL = '/login'
REGISTRATION_URL = '/registration'
LOGOUT_URL = '/logout'

# Tasks
TASKS_URL = "#!/taskman"
DONE_TASKS_URL = "#!/taskman/done-perfor"
TASK_IN_PROGRESS_URL = "#!/taskman/open-perfor"

# Orders
ORDERS_URL = "#!/orders"

# Shop
SHOP_URL = "#!/shop"
SALES_URL = "#!/shop"

# Warehouse
WAREHOUSE_URL = '#!/warehouse'
WH_RESIDUE_URL = '#!/warehouse/residue'
WH_POSTING_URL = "#!/warehouse/posting"
WH_WRITE_OFF_URL = "#!/warehouse/outcome"
WH_MOVE_URL = "#!/warehouse/move"
WH_INVENTORY_URL = "#!/warehouse/stocktaking"
WH_SUPPLIER_REFUNDS_URL = "#!/warehouse/supplier_refunds"
WH_STOCK_SETTING_URL = "#!/warehouse/settings"

# Clients
CLIENT_URL = "#!/clients"

# Payments
CASHBOX_URL = "#!/payments"
INVOICES_URL = "#!/payments/invoices"
REFUND_URL = "#!/payments/refunds"

REPORTS_URL = "#!/reports"

SETTINGS_COMMON_URL = "#!/settings"
SETTINGS_GENERAL_URL = f"{SETTINGS_COMMON_URL}/general"
SETTINGS_BRANCH_URL = f"{SETTINGS_COMMON_URL}/branch"
SETTINGS_LOCATIONS_URL = SETTINGS_BRANCH_URL
SETTINGS_EMPLOYEE_URL = f"{SETTINGS_COMMON_URL}/employee"
SETTINGS_STATUS_URL = f"{SETTINGS_COMMON_URL}/statuses"
SETTINGS_TAGS_URL = f"{SETTINGS_COMMON_URL}/tags/payments"
SETTINGS_NOTIFICATIONS_URL = f"{SETTINGS_COMMON_URL}/notifications/orders"
SETTINGS_SERVICES_URL = f"{SETTINGS_COMMON_URL}/services-pricelist"
SETTINGS_BOOK_URL = f"{SETTINGS_COMMON_URL}/book"
SETTINGS_FORM_EDITOR_URL = f"{SETTINGS_COMMON_URL}/fe"
SETTINGS_TEMPLATES_URL = f"{SETTINGS_COMMON_URL}/document-templates"
SETTINGS_PRICE_AND_DISCOUNT_URL = f"{SETTINGS_COMMON_URL}/prices"
SETTINGS_MARKETING_URL = f"{SETTINGS_COMMON_URL}/marketing"
SETTINGS_INTEGRATIONS_URL = f"{SETTINGS_COMMON_URL}/integrations"
SETTINGS_API_URL = f"{SETTINGS_COMMON_URL}/api"
SETTINGS_LICENSE_URL = f"{SETTINGS_COMMON_URL}/license"
SETTINGS_REFERRALS_URL = f"{SETTINGS_COMMON_URL}/referrals"
SETTINGS_PARTNERS_URL = SETTINGS_REFERRALS_URL
