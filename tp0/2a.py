from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    catch_prob = []
    condition_list = []
    error = []
    for condition in StatusEffect:
        data = []
        condition_list.append(str(condition.name))
        for _ in range(2000):
            caterpie = factory.create("caterpie", 100, condition, 1)
            value = 1.0 if attempt_catch(caterpie, "pokeball", 0.15)[0] else 0.0
            data.append(value)
            # attempt_catch_by_pokeball.append(value)
            # data.append(attempt_catch(caterpie, "heavyball", 0.15)[1])
        catch_prob.append(sum(data) / len(data))
        error.append(np.std(data)/np.sqrt(len(data)))
        print(np.std(data))
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=condition_list, y=catch_prob, name='Catch Probability vs Health Condition',
        error_y = dict(
            type='data',
            array=error,
            visible=True
        )
    ))
    fig.update_layout(title='Catch Probability vs Health Condition')
    fig.show()
