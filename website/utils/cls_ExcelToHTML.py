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

    def to_html(self):
        """Convertit le DataFrame en tableau HTML."""
        # Filtrer les colonnes
        df_filtered = self.df[self.columns]
        
        # Commencer la table HTML
        html_output = "<table border='1' style='border-collapse: collapse;'>"
        
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
