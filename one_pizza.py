from itertools import combinations


class Client:
    def __init__(self, likes, dislikes=None):
        if dislikes is None:
            dislikes = []
        self.likes = likes
        self.dislikes = dislikes

    def likes_pizza(self, pizza):
        """Returns True if the client likes the given pizza, False otherwise."""
        # All ingredients the Client likes must be in.
        for ing in self.likes:
            if ing not in pizza:
                return False
        # None of the ingredients the Client dislikes should be in.
        for ing in self.dislikes:
            if ing in pizza:
                return False
        # If all the above fail, return True.
        return True

    def __repr__(self):
        return 'Client likes:' + str(self.likes) + ' Client dislikes' + str(self.dislikes)


ingredients = set()
C = input()

clients = []
for i in range(int(C)):
    liked = input().split(' ')[1:]
    for ing in liked:
        ingredients.add(ing)

    disliked = input().split(' ')[1:]
    for ing in disliked:
        ingredients.add(ing)

    clients.append(Client(liked, disliked))

# Brute force, try all possible combinations and keep the one with the highest popularity.
popularity_max = 0
best_pizza = []
for r in range(1, len(ingredients) + 1):
    pizzas = combinations(ingredients, r)
    for pizza in list(pizzas):
        clients_liked_pizza = [clients[i].likes_pizza(pizza) for i in range(len(clients))]
        popularity = sum(clients_liked_pizza)
        if popularity_max < popularity:
            popularity_max = popularity
            best_pizza = pizza

print(len(best_pizza), ' '.join(best_pizza))
