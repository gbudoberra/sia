from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import plotly.express as px

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    catch_prob = []
    condition_list = []
    for condition in StatusEffect:
        average = []
        condition_list.append(str(condition.name))
        for _ in range(2000):
            onix = factory.create("onix", 100, condition, 1)
            value = 1 if attempt_catch(onix, "pokeball", 0.15)[0] else 0
            average.append(value)
            # attempt_catch_by_pokeball.append(value)
            # average.append(attempt_catch(onix, "heavyball", 0.15)[1])
        catch_prob.append(sum(average) / len(average))
    fig = px.scatter(x=condition_list, y=catch_prob, labels={'x': 'Health Condition', 'y': 'Catch Probability'})
    fig.update_layout(title='Catch Probability vs Health Condition')
    fig.show()
