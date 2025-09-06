import random

objects = [
    "Virat Kohli", "Narendra Modi", "Shahrukh Khan", "Elon Musk",
    "Ambani", "Rahul Gandhi", "Donald Trump", "Taylor Swift",
    "Iron Man", "Spider-Man", "Tom and Jerry", "Doraemon",
    "A random cow", "A talking parrot", "A robot dog",
    "A cricket fan", "A college student", "A rickshaw driver",
    "A lost astronaut", "A vegetable seller", "Santa Claus",
    "Baba Ramdev", "Motu Patlu", "Shinchan", "Captain Jack Sparrow",
    "A confused goat", "A gamer boy", "Chhota Bheem",
    "A lazy panda", "A dancing elephant", "A hungry monkey",
    "Michael Jackson’s ghost", "A giant lizard", "A YouTuber",
    "A failed magician", "Harry Potter", "A TikTok influencer",
    "A baby crying loudly", "A politician in disguise", "A pizza delivery guy",
    "A nervous teacher", "A Bollywood hero", "An alien from Mars",
    "A sleepy cat", "A ninja turtle", "A robot vacuum cleaner",
    "A crazy scientist", "A lost tourist", "A street dog",
    "A DJ snake", "A giant chicken", "A banana thief"
]

actions = [
    "drives a cycle", "eats 50 samosas", "dances on the street",
    "sings in the railway station", "starts selling pani puri",
    "plays cricket with kids", "cooks biryani", "opens a tea stall",
    "argues with a traffic police", "sleeps in the park",
    "launches a rocket", "does yoga with monkeys", "runs a marathon",
    "paints walls", "becomes a DJ", "sings rap songs",
    "teaches maths in school", "drives an auto", "becomes a barber",
    "joins a circus", "orders pizza for everyone", "starts a dance battle",
    "steals ice cream", "becomes a TikTok star", "opens a gym for dogs",
    "fights with robots", "starts a pillow fight", "catches Pokémon",
    "watches cartoons all day", "buys 1000 bananas", "sells WiFi",
    "becomes a magician", "wins a pani puri competition", "rides a donkey",
    "sings bhajans loudly", "jumps into a swimming pool", "hacks a computer",
    "steals shoes from temple", "eats momos non-stop", "becomes a chef",
    "opens a samosa factory", "plays PUBG all night", "argues with Alexa",
    "orders Zomato for cows", "starts laughing alone", "sleeps in a metro",
    "dances like Michael Jackson", "makes memes all day", "opens a chai stall",
    "starts selling mangoes", "paints his face green", "does stand-up comedy"
]

places = [
    "in Gujarat", "in Mumbai", "in Delhi", "in Bangalore",
    "in Kolkata", "in Jaipur", "in London", "in New York",
    "in Dubai", "in Pakistan", "on the moon", "on Mars",
    "in a zoo", "in a cinema hall", "at railway station",
    "inside a temple", "in the classroom", "at the beach",
    "at a wedding", "in Antarctica", "inside a video game",
    "in Hogwarts", "at Disneyland", "on a moving train",
    "in the jungle", "on top of Mount Everest", "inside a spaceship",
    "in IPL stadium", "at a haunted house", "under the sea",
    "at a shopping mall", "in a traffic jam", "in a 5-star hotel",
    "inside a PUBG map", "in Minecraft world", "at a bus stop",
    "at a pani puri stall", "inside a jail", "in the desert",
    "at a comedy show", "in a cricket stadium", "inside a library",
    "on a skyscraper", "at a police station", "in a TikTok video",
    "at India Gate", "in a metro train", "at Gateway of India",
    "at a pizza shop", "inside a hospital", "in a WhatsApp group"
]

while True:
    obj = random.choice(objects)   
    act = random.choice(actions)   
    place = random.choice(places)  

    headline = f"BREAKING NEWS : {obj} {act} {place}"

    print("\n" + headline)

    user_input = input("Do you want another headline ? (yes/no): ").strip().lower()

    if user_input == "no":
        break

print("\nThanks for using the fake news headline generator... Have a fun day 🎉")
