from com.haneul.models.matjip.dataset import Dataset
import pandas as pd

class MatjipService:
    dataset = Dataset()

    def new_model(self, haneul) -> object:
        this = self.dataset
        this.context = 'C:\\Users\\bitcamp\\Documents\\titanic\\com\\haneul\\datas\\matjib\\'
        this.haneul = haneul
        return pd.read_csv(this.context + this.haneul)
    