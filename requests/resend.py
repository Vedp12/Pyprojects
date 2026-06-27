# import resend


# api_key = "re_b5QefRyA_ArmVVKq9VjhqtPsuPaGU92bQ"

import resend

resend.api_key = "re_b5QefRyA_ArmVVKq9VjhqtPsuPaGU92bQ"

resend.create({
    "name": "Hello , Mr. pravin",
    "html": "<p>Name: pravin</p><p>Total: 100</p>",
    "variables": [
        {
            "key": "PRODUCT",
            "type": "string",
            "fallback_value": "item",
        },
        {
            "key": "PRICE",
            "type": "number",
            "fallback_value": 20,
        },
    ],
})