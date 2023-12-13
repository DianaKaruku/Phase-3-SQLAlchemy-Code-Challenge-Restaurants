# test.py

from models import Restaurant, Customer, Review, session

# Query and test the methods
customer = session.query(Customer).first()
restaurant = session.query(Restaurant).first()
print(customer.full_name())
print(customer.favorite_restaurant().name if customer.favorite_restaurant() else "No favorite restaurant")
print(restaurant.all_reviews())

# Add a new review
customer.add_review(restaurant, rating=5)

# Delete all reviews for a restaurant
customer.delete_reviews(restaurant)

# Commit changes to the database
session.commit()
