from tkinter import Message
import pandas
import random

class AbsDataManager():
    def __init__(self,file_name="Palabras mas frecuentes de ingles - Hoja 1.csv"):
        self.file_name = file_name
        try:
            self.__load_file()
        except FileNotFoundError:
            self.__create_file()
        #except pandas.errors.EmptyDataError:
            #except Exception as ex:
            #print(ex,"Error class = ",type(ex).__name__)  
        
    def __create_file(self):
        with open(f"data/{self.file_name}", "w") as file:
            file.write("")
 
    def __load_file(self):

        try:
            df = pandas.read_csv(f"data/{self.file_name}")

            self.data_dict = {row.English: row.Sphanish for (index, row) in df.iterrows()}
        except FileNotFoundError:
            self.__create_file()
            self.__load_file()
        except pandas.errors.EmptyDataError:
            self.data_dict = {}

    def save_data(self,data={}):
        #Data dict {'English_word':'Sphanish_word'}
        try:
            self.__create_file() #As a clean before to set data
            self.data_dict.update(data)
            df = pandas.DataFrame({
                'English':list(self.data_dict.keys()),#it's necesary convert into a list
                'Sphanish':list(self.data_dict.values()),
                })
            df.to_csv(f"data/{self.file_name}")
        except FileNotFoundError:
            messegue = "No data in database"

    def delete(self,*args):
        try:
            poped = [self.data_dict.pop(key) for key in args]
            self.save_data()
        except KeyError:
            poped = f"Hi there :) = KeyError, key(s)...\n{args}\n...seted dosen't exist.\n Att Rychy ;)"
        return poped

class AllWords(AbsDataManager):
    def __init__(self):
        super().__init__(file_name="frecuently_words_english.csv")

class KnowWords(AbsDataManager):
    def __init__(self):
        super().__init__(file_name="know_words.csv")

class UnknowWords(AbsDataManager):
    def __init__(self):
        super().__init__(file_name="unknow_words.csv")

class DataManager():   
    def __init__(self):
        self.know_words = KnowWords()
        self.unknow_words = UnknowWords()
        self.all_words = AllWords()

    def all_words(self):
        return self.all_words.data_dict
        #return self.unKnow_words().all_words() both clases, have this method
        
        #return super().all_words()     is other option to call an superior method, but now data manger is't an iterence
        #of the AbsDataManger
    def nex_word(self):
        words = self.read_unknow_words()
        self.english = list(words.keys())
        self.sphanish = list(words.values())

        self.index = random.randint(0,len(self.english))
        return ([self.english[self.index],self.sphanish[self.index]])

    def read_know_words(self):
        return self.know_words.data_dict
    
    def read_unknow_words(self):
        return self.unknow_words.data_dict
    
    def save_know_words(self,data):
        return self.know_words.save_data(data)
   
    def save_unkow_words(self,data):
        return self.unknow_words.save_data(data)

    def delete_know_words(self,*args):
        return self.know_words.delete(*args)

    def delete_unknow_words(self,*args):
        #Data dict {'English_word':'Sphanish_word'}
        returning = None
        try:
            self.save_know_words({f"{self.english[self.index]}":f"{self.sphanish[self.index]}"})
            returning = self.unknow_words.delete(*args)
        except IndexError:
            returning = "Index Key wrong"

        return returning

def test_module():
    data = DataManager()
    #data.all_words()
    print("\n")
    data.save_know_words({'Hello':'Hola','Blue':'Azul',})
    print(data.read_know_words())
    data.save_know_words({'Computer':'Computadora','Table':'Mesa',})
    print(data.read_know_words())
    print(data.delete_know_words('Table','Hello'))
    print(data.read_know_words())
    print(data.delete_unknow_words('Table','Hello'))
    print(data.read_unknow_words())

#test_module()