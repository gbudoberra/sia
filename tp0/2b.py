from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import plotly.express as px

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    catch_prob=[]
    for i in range(100):
        average = []
        for _ in range(2000):
            caterpie = factory.create("caterpie", 100, StatusEffect.NONE, 0.01*i)
            value = 1 if attempt_catch(caterpie, "pokeball", 0.15)[0] else 0
            average.append(value)
            # attempt_catch_by_pokeball.append(value)
            # average.append(attempt_catch(caterpie, "heavyball", 0.15)[1])
        catch_prob.append(sum(average) / len(average))
    fig = px.scatter(x=range(100), y=catch_prob, labels={'x': 'HP', 'y': 'Catch Probability'})
    fig.update_layout(title='Catch Probability vs HP')
    fig.show()
