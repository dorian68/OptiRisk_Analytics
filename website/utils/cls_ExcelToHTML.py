import pandas as pd

class ExcelToHTML:
    def __init__(self, df, columns=None, style=None):
        """
        Paramètres :
        - df : DataFrame à convertir en tableau HTML.
        - columns : Liste des colonnes à afficher. Si None, toutes les colonnes seront incluses.
        - style : Dictionnaire de styles CSS à appliquer (par exemple, {'font-weight': 'bold'}).
        """
        self.df = df
        self.columns = columns if columns else df.columns.tolist()
        self.style = style if style else {}

    def _apply_styles(self):
        """Applique le style aux cellules du tableau."""
        styles = ""
        for key, value in self.style.items():
            styles += f"{key}: {value}; "
        return styles


        import pandas as pd

    def generate_pivot_html(self, index_labels, column_labels, value_labels, aggfunc='sum'):
        """
        Génère un tableau croisé dynamique stylisé en HTML.

        :param df: DataFrame d'entrée.
        :param index_labels: Liste des colonnes à utiliser comme index (lignes).
        :param column_labels: Liste des colonnes à utiliser comme colonnes.
        :param value_labels: Liste des colonnes à utiliser comme valeurs.
        :param aggfunc: Fonction d'agrégation (par défaut 'sum', mais peut être 'mean', 'count'...).
        :return: HTML du tableau stylisé.
        """
        
        # Création du tableau croisé dynamique
        pivot_table = pd.pivot_table(self.df, 
                                    values=value_labels, 
                                    index=index_labels, 
                                    columns=column_labels, 
                                    aggfunc=aggfunc, 
                                    fill_value=0)

        # Ajout de styles CSS pour l'affichage
        styled_table = pivot_table.style.set_table_styles([
            {"selector": "thead th", "props": [("background-color", "#43438A"),
                                            ("color", "white"),
                                            ("text-align", "center"),
                                            ("font-weight", "bold"),
                                            ("border", "1px solid black")]},
            {"selector": "tbody td", "props": [("border", "1px solid black"),
                                            ("text-align", "center"),
                                            ("padding", "5px")]},
            {"selector": "tbody tr:nth-child(even)", "props": [("background-color", "#f2f2f2")]},
            {"selector": "tbody tr:hover", "props": [("background-color", "#ddd")]}
        ]).set_table_attributes("class='table table-bordered table-hover'")

        return styled_table.to_html()

    def to_html(self):
        """Convertit le DataFrame en tableau HTML."""
        # Filtrer les colonnes
        df_filtered = self.df[self.columns]

        print(self.df)


        # Extrait arbitrairement les trois premières colonnes
        a, b, c,d = df_filtered.columns[:4]

        # Construit le TCD
        tcd = pd.pivot_table(self.df,[d],[b,c],[a],'sum').fillna(0)

        columns_tcd = [col for _, col in tcd.columns]
        
        # Commencer la table HTML
        html_output = "<table border='1' style='border-collapse: collapse;border: 2px solid skyblue'>"
        
         # Entête du tableau
        html_output += "<thead><tr>"
        for col in columns_tcd:
            print(col)
            html_output += f"<th style='{self._apply_styles()}'>{col}</th>"
        html_output += "</tr></thead>"
        
        # Corps du tableau
        html_output += "<tbody>"
        print(tcd)
        for _, row in tcd.iterrows():
            print(f"this is _ {_}")
            html_output += "<tr>"
            for elem in _:
                print(f"this elem {elem}")
                html_output += f"<td style='{self._apply_styles()}'>{elem}</td>"
            for col in columns_tcd:
                print(f"this is col {col}")
                html_output += f"<td style='{self._apply_styles()}'>{row.values[columns_tcd.index(col)]}</td>"
            html_output += "</tr>"
        html_output += "</tbody>"

        # Fin de la table HTML
        html_output += "</table>"
        
        return html_output
        """
        # Entête du tableau
        html_output += "<thead><tr>"
        for col in df_filtered.columns:
            html_output += f"<th style='{self._apply_styles()}'>{col}</th>"
        html_output += "</tr></thead>"
        
        # Corps du tableau
        html_output += "<tbody>"
        for _, row in df_filtered.iterrows():
            html_output += "<tr>"
            for col in df_filtered.columns:
                html_output += f"<td style='{self._apply_styles()}'>{row[col]}</td>"
            html_output += "</tr>"
        html_output += "</tbody>"

        # Fin de la table HTML
        html_output += "</table>"
        
        return html_output
        """
