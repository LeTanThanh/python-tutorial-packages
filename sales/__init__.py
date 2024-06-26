# import the order module automatically
from sales.order.order import create_sales_order

# default sales tax rate
TAX_RATE = 0.07

__all__ = [
  "order",
  "delivery"
]
