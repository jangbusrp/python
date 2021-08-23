# def man(f):
#     def wrapper():
#         print("this is me:")
#         f()
#         print("Last")
#     return wrapper

# @man
# def fun():
#     print("hello world:")

# @man
# def cal():
#     print("successful")    

# fun()
# cal()


def login_required(func):
    	def wrapper(user):
            admin = "ram"
            if user == admin:
                return func(user)
            else:
                return (f"sorry {user} is not authenicated for this view")
            
def product_view(user):
	print(f"welcome {user}")
	print("list of products:")

@login_required
def sale_report_view(user):
	print(f"welcome {user}")
	print("showing sales report")

@login_required
def price_history(user):
	print(f"welcome {user}")
	print("showing price history")

print(product_view("hari"))
print(sale_report_view("hari"))
print(price_history("ram"))
