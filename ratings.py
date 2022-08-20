"""Restaurant rating lister."""
import random
import sys

def make_restaurant_ratings_pairs(filename = sys.argv[1]):
	restaurants = open(filename)
	restaurant_and_rating = {}

	for line in restaurants:
		restaurant, rating = line.rstrip().split(':')
		restaurant_and_rating[restaurant] = rating

	restaurants.close()
	return restaurant_and_rating


def print_restaurant_ratings():

	restaurant_dict = make_restaurant_ratings_pairs()

	sorted_restaurant_and_rating = sorted(restaurant_dict.items())

	for restaurant_tuple in sorted_restaurant_and_rating:
		name, score = restaurant_tuple
		print(f"{name} is rated at {score}.")


def adds_restaurant_ratings():
	restaurant = input("Enter a restaurant name: ")

	while True:
		rating = int(input("Enter a rating: "))

		if rating > 5 or rating < 1:
			print("Pls enter 1 to 5")
		else:
			break

	restaurant_and_ratings = make_restaurant_ratings_pairs()
	restaurant_and_ratings[restaurant] = rating
	print_restaurant_ratings()
	print(f"{restaurant} is rated at {rating}")

def update_random_restaurant():

	restaurant_and_ratings = make_restaurant_ratings_pairs()
	restaurant_names = list(restaurant_and_ratings.keys())

	restaurant_name_change = random.choice(restaurant_names)

	print(f"{restaurant_name_change} was originally rated at \
{restaurant_and_ratings[restaurant_name_change]}")

	while True:
		rating = int(input("Enter a new rating: "))

		if rating > 5 or rating < 1:
			print("Pls enter 1 to 5")
		else:
			break

	restaurant_and_ratings[restaurant_name_change] = rating

	print(f"{restaurant_name_change} is now rated at \
{restaurant_and_ratings[restaurant_name_change]}")

	user_choices()


def user_choices():
	choices = input("Would you like to A) See all ratings B) Add restaurant or \
C) Update random restaurant or D) Quit ")
	if choices == "A":
		print_restaurant_ratings()

	elif choices == "B":
		adds_restaurant_ratings()

	elif choices == "C":
		update_random_restaurant()

	elif choices == "D":
		return None

user_choices()

