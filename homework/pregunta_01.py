import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    df = pd.read_csv("files/input/shipping-data.csv")

    os.makedirs("docs", exist_ok=True)

    # 1. shipping_per_warehouse.png
    plt.figure(figsize=(8, 5))
    df["Warehouse_block"].value_counts().plot(kind="bar")
    plt.title("Shipping per Warehouse")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

    # 2. mode_of_shipment.png
    plt.figure(figsize=(8, 5))
    df["Mode_of_Shipment"].value_counts().plot(kind="bar")
    plt.title("Mode of Shipment")
    plt.xlabel("Mode")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    # 3. average_customer_rating.png
    plt.figure(figsize=(8, 5))
    df["Customer_rating"].plot(kind="hist", bins=5)
    plt.title("Average Customer Rating")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

    # 4. weight_distribution.png (CORRECTO SEGÚN EL TEST)
    plt.figure(figsize=(8, 5))
    df["Weight_in_gms"].plot(kind="hist", bins=20)
    plt.title("Weight Distribution")
    plt.xlabel("Weight (g)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()

    # HTML Dashboard
    html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Shipping Dashboard</title>
</head>
<body>
    <h1>Shipping Dashboard</h1>

    <h2>Shipping per Warehouse</h2>
    <img src="shipping_per_warehouse.png">

    <h2>Mode of Shipment</h2>
    <img src="mode_of_shipment.png">

    <h2>Average Customer Rating</h2>
    <img src="average_customer_rating.png">

    <h2>Weight Distribution</h2>
    <img src="weight_distribution.png">

</body>
</html>
"""

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)
