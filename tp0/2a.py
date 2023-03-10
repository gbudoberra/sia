from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import plotly.express as px

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    catch_prob=[]
    for i in range(100):
        average = []
        for _ in range(100):
            onix = factory.create("onix", 100, StatusEffect.NONE, 0.01*i)
            average.append(attempt_catch(onix, "heavyball", 0.15)[1])
        catch_prob.append(sum(average) / len(average))
    fig = px.scatter(x=range(100), y=catch_prob, labels={'x': 'HP', 'y': 'Catch Probability'})
    fig.show()
