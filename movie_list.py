import movie
import fresh_tomatoes

# Creating movie objects
race_gurram=movie.Movie("Race Gurram",
                        "https://i.ytimg.com/vi/db_2mujPXjk/movieposter.jpg",
                        "https://www.youtube.com/watch?v=yCt-YUbs7H4")
so_satyamurty=movie.Movie("S/O Satyamurthy",
                "https://upload.wikimedia.org/wikipedia/en/9/94/SO_Satyamurthy_soundtrack.jpg",
                "https://www.youtube.com/watch?v=dpnENU952gc")

sarainodu=movie.Movie("Sarainodu",
                "https://2.bp.blogspot.com/-1uYsDlTbElI/VsKdvn-qn8I/AAAAAAAAA-s/5gniTTiOEt0/s1600/allu-arjun-Sarrainodu-film-New-Wallpapers-hd.jpg", # noqa
                "https://www.youtube.com/watch?v=SquY-O70Feo")

aarya_2=movie.Movie("Aarya 2",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjkwNWEyYTQtZTUyOS00MTg5LTk3YjQtOTY3ZjlhZmE5MjFmXkEyXkFqcGdeQXVyMzA0NTI2OTM@._V1_UY268_CR9,0,182,268_AL_.jpg", #noqa
                "https://www.youtube.com/watch?v=vpfXFqlLA3A")

# Storing movie objects in a list
movies=[race_gurram,so_satyamurty,sarainodu,aarya_2]
# Calling method from fresh tomatoes
fresh_tomatoes.open_movies_page(movies)
