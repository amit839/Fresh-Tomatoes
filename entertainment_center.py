import media, fresh_tomatoes

hobbs_and_shaw = media.Movie("Fast & Furious Presents: Hobbs & Shaw",
    "Ever since hulking lawman Hobbs (Johnson), a loyal agent of America's Diplomatic Security Service, and lawless outcast Shaw (Statham), a former British military elite operative, first faced off in 2015’s Furious 7, the duo have swapped smack talk and body blows as they’ve tried to take each other down. But when cyber-genetically enhanced anarchist Brixton (Idris Elba) gains control of an insidious bio-threat that could alter humanity forever — and bests a brilliant and fearless rogue MI6 agent (The Crown’s Vanessa Kirby), who just happens to be Shaw’s sister — these two sworn enemies will have to partner up to bring down the only guy who might be badder than themselves.",
    "https://upload.wikimedia.org/wikipedia/en/0/00/Fast_%26_Furious_Presents_Hobbs_%26_Shaw_-_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=HZ7PAyCDwEg")

spider_man = media.Movie("Spider-Man: Far From Home",
    "Following the events of Avengers: Endgame, Spider-Man must step up to take on new threats in a world that has changed forever.",
    "https://upload.wikimedia.org/wikipedia/en/b/bd/Spider-Man_Far_From_Home_poster.jpg",
    "https://www.youtube.com/watch?v=Nt9L1jCKGnE")

avengers_infinity_war = media.Movie("Avengers: Infinity War",
    "The Avengers must stop Thanos and his army from acquiring all the infinity stones. But the mad Titan is prepared to go to any lengths in order to do what he thinks is necessary.",
    "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

avengers_end_game = media.Movie("Avengers: Endgame",
    "Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle.",
    "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg",
    "https://www.youtube.com/watch?v=TcMBFSGVi1c")

john_wick = media.Movie("John Wick: Chapter 3 – Parabellum",
    "After gunning down a member of the High Table -- the shadowy international assassin's guild -- legendary hit man John Wick finds himself stripped of the organization's protective services. Now stuck with a $14 million bounty on his head, Wick must fight his way through the streets of New York as he becomes the target of the world's most ruthless killers.",
    "https://upload.wikimedia.org/wikipedia/en/9/94/John_Wick_Chapter_3_Parabellum.png",
    "https://www.youtube.com/watch?v=pU8-7BX9uxs")

lion_king = media.Movie("The Lion King",
    "Simba idolizes his father, King Mufasa, and takes to heart his own royal destiny on the plains of Africa. But not everyone in the kingdom celebrates the new cub's arrival. Scar, Mufasa's brother -- and former heir to the throne -- has plans of his own. The battle for Pride Rock is soon ravaged with betrayal, tragedy and drama, ultimately resulting in Simba's exile. Now, with help from a curious pair of newfound friends, Simba must figure out how to grow up and take back what is rightfully his.",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/Disney_The_Lion_King_2019.jpg",
    "https://www.youtube.com/watch?v=7TavVZMewpY")

list_of_movies = [avengers_end_game, avengers_infinity_war, lion_king, hobbs_and_shaw, john_wick, spider_man]

fresh_tomatoes.open_movies_page(list_of_movies)
