from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Générer et afficher le graphique catégoriel
cat_fig = draw_cat_plot()
cat_fig.savefig('catplot.png')
cat_fig.show()

# Générer et afficher la carte thermique
heat_fig = draw_heat_map()
heat_fig.savefig('heatmap.png')
heat_fig.show()
