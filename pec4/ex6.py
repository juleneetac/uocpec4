import folium
import pandas as pd
import io
from PIL import Image
import selenium


# Ejercicio 6: Mapas coropléticos (1.5 puntos)

def print_map(df: pd.DataFrame, column_keep: str) -> None:
    # initialize the map and store it in a m object
    m = folium.Map(location=[40, -95], zoom_start=4)
    url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
    )
    state_geo = f"{url}/us-states.json"

    # Se comprueba que la columna "pop_2014" existe en el DataFrame
    if column_keep not in df.columns:
        raise ValueError("La columna {} no existe en el DataFrame.".format(column_keep))
    df_cleaned = df[["code", column_keep]]

    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=df_cleaned,
        columns=["code", column_keep],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=.1,
        legend_name="{} Rate (%)".format(column_keep),
    ).add_to(m)

    folium.LayerControl().add_to(m)

    # show the map
    m

    # save html
    html_save_path = "./data/{}.html".format(column_keep)
    m.save(html_save_path)
    print("HTML file saved in {}".format(html_save_path))

    # save image
    img_data = m._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img_save_path = "./data/{}.png".format(column_keep)
    print("Image file saved in {}".format(img_save_path))
    img.save(img_save_path)

