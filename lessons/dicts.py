"""Practicing dicts."""


icecreamBuyers: dict[str, float] = {"chocolate": "12", "vanilla": "8", "strawberry": "5"}
icecreamBuyers["mint"] = 3
icecreamBuyers.pop("mint")
icecreamBuyers["chocolate"]
icecreamBuyers["vanilla"] = 10
len(icecreamBuyers)
"mint" in icecreamBuyers
"chocolate" in icecreamBuyers
if "mint" in icecreamBuyers:
    print(icecreamBuyers["mint"])
else:
    print("no orders of mint")