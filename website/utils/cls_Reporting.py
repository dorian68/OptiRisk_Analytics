from abc import ABC, abstractmethod

#https://www.docstring.fr/glossaire/classe-abstraite/

class Reporting:
    @abstractmethod
    def to_html(self):
        pass
    
    @abstractmethod
    def to_csv(self):
        pass

    @abstractmethod
    def col_to_base(self):
        pass

    @abstractmethod
    def run(self):
        pass 

    @abstractmethod
    def load_format_excel(self):
        pass
    
class RiskReport(Reporting):
    def __init__(self,name,source_file,source_file_col):
        self.name = name
        self.source_file = source_file
        self.source_file_col = source_file_col

    def to_html(self):
        return super().to_html()
    
    def to_csv(self):
        return super().to_csv()
    
    def col_to_base(self):
        return super().col_to_base()
    
    def run(self):
        return 0
    
    def load_format_excel(self):
        return super().load_format_excel()
    
class ForecastTreasury(Reporting):
    def to_html(self):
        return super().to_html()
    
    def to_csv(self):
        return super().to_csv()
    
    def col_to_base(self):
        return super().col_to_base()
    
    def forecastTreasury(self):
        return 0
    
    def load_format_excel(self):
        return super().load_format_excel()
    
class PerfReport(Reporting):
    def to_html(self):
        return super().to_html()
    
    def to_csv(self):
        return super().to_csv()
    
    def col_to_base(self):
        return super().col_to_base()
    
    def run_perf(self):
        return 0
    
    def load_format_excel(self):
        return super().load_format_excel()

