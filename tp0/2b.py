from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import plotly.graph_objects as go
import numpy as np


if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    catch_prob = []
    error = []
    x = []
    for i in range(100):
        data = []
        x.append(i)
        for _ in range(1000):
            caterpie = factory.create("caterpie", 100, StatusEffect.NONE, 0.01*i)
            value = 1 if attempt_catch(caterpie, "pokeball", 0.15)[0] else 0
            data.append(value)
            # attempt_catch_by_pokeball.append(value)
            # data.append(attempt_catch(caterpie, "heavyball", 0.15)[1])
        catch_prob.append(sum(data) / len(data))
        error.append(np.std(data)/np.sqrt(len(data)))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=catch_prob, name='Catch Probability vs HP',
                     error_y=dict(
                         type='data',
                         array=error,
                         visible=True
                     )
                     ))
    fig.update_layout(title='Catch Probability vs HP')
    fig.show()
