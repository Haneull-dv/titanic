from com.haneul.models.titanic.dataset import Dataset
import pandas as pd

"""
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼

print(f'결정트리 활용한 검증 정확도 {None}')
print(f'랜덤포레스트 활용한 검증 정확도 {None}')
print(f'나이브베이즈 활용한 검증 정확도 {None}')
print(f'KNN 활용한 검증 정확도 {None}')
print(f'SVM 활용한 검증 정확도 {None}')
"""

class TitanicService:
    dataset = Dataset()

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = 'C:\\Users\\bitcamp\\Documents\\titanic\\com\\haneul\\datas\\titanic\\'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)
    
    def preprocess(self, train_fname, test_fname) -> object:
        print("--------------- 모델 전처리 시작 ---------------")
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age',
                    'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        this = self.dataset
        this.train = self.new_model(train_fname)
        this.test = self.new_model(test_fname)
        this.id = this.test['PassengerId']
        # 'Sibsp', 'Parch', 'Cabin', 'Ticket' 지워야됨
        drop_features = ['SibSp', 'Parch', 'Ticket','Cabin']
        this = self.drop_feature(this, *drop_features)
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate_title(this)
        this = self.title_nominal(this, title_mapping)
        this = self.gender_nominal(this)
        this = self.embarked_nominal(this)
        # self.df_info(this)
        this = self.age_ratio(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        this = self.drop_feature(this, "Name", "Sex", "Age", "Fare")
        return this
 

    @staticmethod
    def create_labels(this) -> object:
        return this.train['Survived']
    
    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)
   
    @staticmethod
    def drop_feature(this, *feature) -> object:
        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]
        return this
    
    @staticmethod
    def extract_title_from_name(this):
        # for i in [this.train, this.text]:
        #    i['title'] = i['Name'].str.extract('([A-Za-z]+)\.', expand=False)
        [i.__setitem__('Title', i['Name'].str.extract('([A-Za-z]+)\.', expand=False)) 
        for i in [this.train, this.test]]
        return this
    
    @staticmethod
    def remove_duplicate_title(this):
        # [set(i['Title']) for i in [this.train, this.test]]
        #     a += set(i['Title']) 
        a = []
        for i in [this.train, this.test]:
            a += list(set(i['Title']))
        a = list(set(a))
        print("❤️❤️❤️")
        print(a)
        # ['Col', 'Don', 'Jonkheer', 'Ms', 'Sir', 'Dr', 'Mrs', 'Lady', 'Miss',
        # 'Mme', 'Mlle', 'Capt', 'Countess', 'Rev', 'Dona', 'Master', 'Major', 'Mr'] 
        '''
        ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
        'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping
    
    @staticmethod
    def title_nominal(this, title_mapping):
        for i in [this.train, this.test]:
            i['Title'] = i['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            i['Title'] = i['Title'].replace(['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme'], 'Rare')
            i['Title'] = i['Title'].replace(['Mlle'], 'Mr')
            i['Title'] = i['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            i['Title'] = i['Title'].fillna(0)
            i['Title'] = i['Title'].map(title_mapping)
            
        return this
    
    @staticmethod
    def gender_nominal(this):
        return this
    
    @staticmethod
    def embarked_nominal(this):
        this.train = this.train.fillna({"Embarked": 'S'}) #사우스햄튼이 가장 많으니까
        this.test = this.test.fillna({"Embarked": 'S'})
        this.train["Embarked"] = this.train["Embarked"].map({'S':1, 'C':2, 'Q':3})
        this.test["Embarked"] = this.test["Embarked"].map({'S':1, 'C':2, 'Q':3})

        return this
    
    @staticmethod
    def age_ratio(this):
        return this

    @staticmethod
    def pclass_ordinal(this):
        return this
    
    @staticmethod
    def fare_ratio(this):
        return this
    
    @staticmethod
    def null_check(this):
        [print(i.isnull().sum(), inplace=True) for i in [this.train, this.test]]
        return this
    





            