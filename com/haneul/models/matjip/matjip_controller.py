from com.haneul.models.matjip.dataset import Dataset
from com.haneul.models.matjip.matjip_service import MatjipService

class MatjipController:
    dataset = Dataset()
    service = MatjipService()

    def modeling(self, matjip):
        this = self.dataset
        this.matjip = self.service.new_model(matjip)
        print("🍴맛집 데이터🍴")
        print(this.matjip)
        return this