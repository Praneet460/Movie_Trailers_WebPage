import media
import fresh_tomatoes
judwaa_2 = media.Movie("Judwaa 2",
                       "Judwaa 2 Official Trailor",
                        "https://upload.wikimedia.org/wikipedia/en/9/91/Judwaa_2_Poster.jpg",
                        "https://www.youtube.com/watch?v=DDwbjWCgxVM")

aksar_2 = media.Movie("Aksar 2",
                       "Aksar 2 Official Trailor",
                        "https://upload.wikimedia.org/wikipedia/commons/c/c7/Aksar_2_Official_Movie_Poster.jpg",
                        "https://www.youtube.com/watch?v=o-owuA1rezY")

bhoomi = media.Movie("Bhoomi",
                       "Bhoomi Official Trailor",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Bhoomi_Poster.jpg",
                        "https://www.youtube.com/watch?v=AgiFCRU0MXg")

baadshaho = media.Movie("Baadshaho",
                       "Baadshaho Official Trailor",
                        "https://upload.wikimedia.org/wikipedia/en/c/ce/Ajay_Devgn%27s_Baadshaho.JPG",
                        "https://www.youtube.com/watch?v=Ny7fULat8ws")

secret_superstar = media.Movie("Secret Superstar",
                       "Secret Superstar Official Trailor",
                        "https://upload.wikimedia.org/wikipedia/en/e/e9/SecretSuperstar.jpg",
                        "https://www.youtube.com/watch?v=J_yb8HORges")

lucknow_central = media.Movie("Lucknow central",
                       "Lucknow Central Official Trailor",
                        "https://upload.wikimedia.org/wikipedia/en/a/a5/Lucknow_Central_-_Poster.jpg",
                        "https://www.youtube.com/watch?v=KAQvmBSzHlI")

simran = media.Movie("Simran",
                       "Simran Official Trailor",
                        "https://upload.wikimedia.org/wikipedia/en/d/d3/Simran_Poster.jpg",
                        "https://www.youtube.com/watch?v=_LUe4r6eeQA")

chef = media.Movie("Chef",
                       "Chef Official Trailor",
                        "https://upload.wikimedia.org/wikipedia/en/b/b8/Chef_2014.jpg",
                        "https://www.youtube.com/watch?v=YaFJXd3ciLs")

newton = media.Movie("Newton",
                       "Newton Official Trailor",
                        "https://upload.wikimedia.org/wikipedia/commons/4/4d/Newton_Film_Poster.jpg",
                        "https://www.youtube.com/watch?v=yU6zMPFd4UU")


movies=[judwaa_2, aksar_2, bhoomi, baadshaho, secret_superstar, lucknow_central, simran, chef, newton]
fresh_tomatoes.open_movies_page(movies)

