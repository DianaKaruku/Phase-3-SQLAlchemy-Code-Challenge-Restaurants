# seeds.py

from models import Restaurant, Customer, Review, session

# Create instances of Restaurant and Customer
restaurant1 = Restaurant(name='Restaurant A', price=2)
restaurant2 = Restaurant(name='Restaurant B', price=3)
restaurant3 = Restaurant(name='Restaurant C', price=4)

customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

# Add reviews
review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=4)
review2 = Review(restaurant=restaurant2, customer=customer1, star_rating=5)
review3 = Review(restaurant=restaurant1, customer=customer2, star_rating=3)

# Add instances to the session
session.add_all([restaurant1, restaurant2, restaurant3, customer1, customer2, review1, review2, review3])

# Commit changes to the database
session.commit()
