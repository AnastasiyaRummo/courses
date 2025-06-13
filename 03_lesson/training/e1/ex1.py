from product import Product


my_product = Product('smartphone', '30 000')
productname = my_product.productName
print(productname)
print(my_product.get_name())
productname = productname + '1'
print(productname)

print(my_product.get_price())
print(my_product.get_info())
