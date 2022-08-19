"""Restaurant rating lister."""
import sys

def print_restaurant_ratings(filename = sys.argv[1]):
	restaurants = open(filename)
	restaurant_and_rating = {}

	for line in restaurants:
		restaurant, rating = line.rstrip().split(':')
		restaurant_and_rating[restaurant] = rating

	sorted_restaurant_and_rating = sorted(restaurant_and_rating.items())

	for restaurant_tuple in sorted_restaurant_and_rating:
		name, score = restaurant_tuple
		print(f"{name} is rated at {score}.")

	restaurants.close()
	return restaurant_and_rating


def adds_restaurant_ratings():
	restaurant = input("Enter a restaurant name: ")

	while True:
		rating = int(input("Enter a rating name: "))

		if rating > 5 or rating < 1:
			print("Pls enter 1 to 5")
		else:
			break

	restaurant_and_ratings = print_restaurant_ratings()
	restaurant_and_ratings[restaurant] = rating
	print(f"{restaurant} is rated at {rating}")

def user_choices():
	choices = input("Would you like to A) See all ratings B) Add restaurant or \
C) Quit ")
	if choices == "A":
		print_restaurant_ratings()

	elif choices == "B":
		adds_restaurant_ratings()

	elif choices == "C":
		return None

user_choices()

