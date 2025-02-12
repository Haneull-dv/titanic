from com.haneul.models.titanic.dataset import Dataset
import pandas as pd

class TitanicService:
    dataset = Dataset()

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = 'C:\\Users\\bitcamp\\Documents\\titanic\\com\\haneul\\datas\\titanic\\'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)


        