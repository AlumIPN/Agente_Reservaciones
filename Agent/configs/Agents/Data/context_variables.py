import datetime

context_variables = {
    "customer_context": {
        "CUSTOMER_ID": "",
        "NAME": "",
        "AGE": "",
        "EMAIL": "",
        "PHONE": ""
    },
    "general_context": {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
}

