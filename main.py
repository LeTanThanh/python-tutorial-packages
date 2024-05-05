if __name__ == "__main__":
  # Importing packages

  """
  import package.module

  package.module.function

  from module import function
  """

  # import sales.billing
  # import sales.delivery
  # import sales.order

  # sales.order.create_sales_order()
  # sales.delivery.create_delivery()
  # sales.billing.create_billing()

  # from sales.order import create_sales_order
  # from sales.delivery import create_delivery
  # from sales.billing import create_billing

  # create_sales_order()
  # create_delivery()
  # create_billing()

  # from sales.order import create_sales_order as create_order
  # from sales.delivery import create_delivery as start_delivery
  # from sales.billing import create_billing as issue_billing

  # create_order()
  # start_delivery()
  # issue_billing()

  # Initializing a package

  from sales import TAX_RATE

  print(TAX_RATE)

  import sales

  sales.order.create_sales_order()
