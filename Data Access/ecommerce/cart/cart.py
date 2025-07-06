from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        ## Functia get poate intoarce o valoare sau None
        cart = request.session.get('cos')
        ## Daca cartul nu e gol
        if not cart:
            request.session['cos'] = cart = {}
        self.cart  = cart

    ### Cartul este un fel de dictionar
    ###  {  "productId1": "3", "productId2":1} 

    def add_product(self, product_id, quantity):
        print('cartul este:', self.cart)
        self.cart[product_id] = self.cart.get(product_id, 0) + int(quantity)
        self.session.modified = True
        print('cartul este:', self.cart)

    def all_products(self):
        print(self.cart)
        product_ids = self.cart.keys()
        print('Cheile sunt:',product_ids)
        ## O luam din baza de date
        product_list = Product.objects.filter(id__in=product_ids)
        product_quantities = []
        for prod in product_list:
            print(prod, prod.id)
            print("self.cart", self.cart)
            quantity = self.cart[str(prod.id)]
            price =  str(prod.price)
            product_quantities.append((prod, quantity, price))
        return product_quantities
    
    def total(self):
        product_quantities = self.all_products()
        suma = 0
        for prod, quantity, price in product_quantities:
            suma += quantity * float(price)
        return suma

    def count(self):
        product_quantities = self.all_products()
        suma = 0
        for prod, quantity, price in product_quantities:
            suma += quantity
        return suma