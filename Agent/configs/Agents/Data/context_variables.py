from datetime import datetime

context_variables = {
    "customer_context": {
        "CUSTOMER_ID":"customer_12345",
        "NAME": "Brandon Giron"
    },
    "general_context":{
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
}