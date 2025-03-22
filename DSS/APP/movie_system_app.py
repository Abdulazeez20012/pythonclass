from datetime import datetime
from DSS.APP.movie_system import MovieSystem

if __name__ == "__main__":
    movie_system = MovieSystem()
    while True:
        print("\n|-----------😎WELCOME TO AZ-FLIX MOVIE SHOW😎-----------|")
        print("1. Add a Movie 📑")
        print("2. Rate a Movie ⁜")
        print("3. Get Average Rating of a Movie ✓")
        print("4. Get Average Rating of All Movies 👌💏🏿💏")
        print("5. View All Movies 😶‍🌫️")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            while True:
                try:
                    title = input("Enter movie title: ").strip().lower()
                    if not title:
                        raise ValueError("Movie title cannot be empty. Please enter a valid title.")
                    movie_system.add_movie(title)
                    print(f"Movie '{title}' added successfully on {datetime.now()}")
                    break
                except ValueError as ve:
                    print(f"Input Error: {ve}")
                except Exception as ex:
                    print(f"An unexpected error occurred: {ex}")

        elif choice == "2":
            while True:
                try:
                    title = input("Enter movie title: ").strip().lower()
                    if not title:
                        raise ValueError("Movie title cannot be empty. Please enter a valid title.")

                    rating_input = input("Enter rating (1-5): ").strip()
                    if not rating_input.isdigit():
                        raise ValueError("Rating must be a number. Please enter a valid rating between 1 and 5.")

                    rating = int(rating_input)
                    if rating < 1 or rating > 5:
                        raise ValueError("Rating must be between 1 and 5. Please enter a valid rating.")

                    movie_system.rate_movie(title, rating)
                    print(f"Rating added to '{title}' successfully!")
                    break
                except ValueError as ve:
                    print(f"Input Error: {ve}")
                except Exception as ex:
                    print(f"An unexpected error occurred: {ex}")

        elif choice == "3":
            while True:
                try:
                    title = input("Enter movie title: ").strip().lower()
                    if not title:
                        raise ValueError("Movie title cannot be empty. Please enter a valid title.")
                    average_rating = movie_system.get_movie_rating(title)
                    print(f"Average rating for '{title}': {average_rating:.2f}")
                    break
                except ValueError as ve:
                    print(f"Input Error: {ve}")
                except Exception as ex:
                    print(f"An unexpected error occurred: {ex}")

        elif choice == "4":
            try:
                average_rating = movie_system.get_all_movies_average_rating()
                print(f"Average rating of all movies: {average_rating:.2f}")
            except Exception as ex:
                print(f"An unexpected error occurred: {ex}")

        elif choice == "5":
            try:
                movies = movie_system.view_all_movies_in_app()
                if movies:
                    print("\nList of Movies:")
                    for movie in movies:
                        print(movie)
                else:
                    print("No movies added yet.")
            except Exception as ex:
                print(f"An unexpected error occurred: {ex}")

        elif choice == "6":
            print("Exiting application...")
            break

        else:
            print("Invalid option, please try again.")
