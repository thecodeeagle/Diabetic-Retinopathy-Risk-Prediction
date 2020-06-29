import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import Image
import csv
import os

Window.clearcolor = (190, 131, 255, 0.76)

class MainPage(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50,15,50,15]
        self.add_widget(Label(text= "Welcome to the Diabetic Retinopathy Detection System! ", color =(0,0,0,1), font_size = "20sp"))
        self.add_widget(Label(text= "Please enter the following details to continue", color =(0,0,0,1)))

        self.add_widget(Label(text ="Patient Name:", color =(0,0,0,1)))
        self.name = TextInput(multiline= False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Patient ID:", color =(0,0,0,1)))
        self.ID = TextInput(multiline=False)
        self.add_widget(self.ID)


        self.join = Button(text = "Join")
        self.join.bind(on_press = self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):
        name = self.name.text
        ID = self.ID.text
        with open("view.txt","a") as f:

            f.write(f"For Mr./Ms. : {name}  with ID: {ID} \n")
        detect_app.screen_manager.current = "Menu"


class Page(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = [10,10]
        self.padding = [20,10,20,10]
        self.message = Label(text="Choose your preferred weighting scheme", color =(0,0,0,1))
        self.add_widget(self.message)
        self.image = Image(source = "retino.jpg", size= (20,20))
        self.add_widget(self.image)
        #self.add_widget(Label())

        self.p_values = Button(text="Based on the p-values of genes involved")
        self.p_values.background_color = (128,0,0,1)
        self.p_values.bind(on_press = self.p_value_button)
        self.add_widget(self.p_values)
        #self.add_widget(Label())

        self.string = Button(text="Based on the string interactions of genes involved")
        self.string.background_color = (128,0,0,1)
        self.string.bind(on_press = self.string_button)
        self.add_widget(self.string)
        #self.add_widget(Label())

        self.back = Button(text="Back")
        self.back.bind(on_press = self.back_button)
        self.add_widget(self.back)

    def back_button(self, instance):
        sm = detect_app.screen_manager.previous()
        detect_app.screen_manager.current = sm



    def p_value_button(self, instance):
        detect_app.screen_manager.current = "P_Value"

    def string_button(self, instance):
        detect_app.screen_manager.current = "String"

class P_Value(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (Window.size[0], self.size[1])
        self.cols = 1
        self.count = -1
        self.score_dict = {'ACE': 0, 'DPP4': 0, 'APOE': 0, 'VEGFA': 0, 'ADM': 0, 'CY2PC19': 0, 'CHN2': 0, 'XRCC1': 0, 'TNFRSF11B': 0, 'ADIPOQ': 0, 'CNR1': 0, 'AKR1B1': 0, 'ALDH2': 0, 'FTO': 0, 'CDKAL1': 0, 'API5': 0, 'ARHGAP22': 0, 'GSTT1': 0}
        self.padding = [20,10,20,10]

        self.header =Label(text ="P-VALUE WEIGHTING SCHEME", color =(0,0,0,1), size_hint_y = None)
        self.add_widget(self.header)
        self.text1 = Label(text= "You will be presented queries for each gene one by one.", color =(0,0,0,1), size_hint_y = None )

        self.add_widget(self.text1)
        self.centre = Image(source="1.png", size=(200,200))
        self.add_widget(self.centre)

        self.text2 = Label(text= "Select YES or NO for each question. The scores will be calculated accordingly", color =(0,0,0,1),  size_hint_y = None)
        self.add_widget(self.text2)

        self.next = Button(text="Next", size_hint_y=None)
        self.next.bind(on_press = self.next_button)
        self.add_widget(self.next)
        new = """Diabetic Retinopathy Risk Score Report

                Method used for Weighing Scores : P-Value Grading

                Grade 1 : P-value <0.001
                Grade 2	:0.001<P-value<0.01
                Grade 3 : P-value >0.01

                Details of genes and scoring scheme"""


        with open("presults.txt",'w') as f:
            f.truncate(0)
            f.write(new)
            f.close()


        self.total_score = 0
        self.score =0



    def display(self, count):
        self.clear_widgets()
        self.clear_widgets()
        self.count = count


        with open('genedetails.csv', 'r') as csv_file, open('presults.txt', 'a') as f:
            self.csv_reader = csv.DictReader(csv_file)
            self.new_reader = list(self.csv_reader)
            row = self.new_reader[self.count]
            self.header =Label(text ="Query for :" + row["GENE SYMBOL"]+ "- " + row["GENE NAME"], color =(0,0,0,1))
            self.add_widget(self.header)

            def on_checkbox_active_one(checkbox_one, value):
                if value:
                    score_ACE(0)
            def on_checkbox_active_two(checkbox_two, value):
                if value:
                    score_ACE(0.5)
            def on_checkbox_active_three(checkbox_three, value):
                if value:
                    score_ACE(1)
            def score_ACE(param):


                self.total_score += param*1
                if param>=0.5:
                    self.score_dict['ACE']= param*1
                    #

            self.i = 0
            if(int(row['No_Of_Q'])==0):
                f.write("\n\n GENE :- ACE - Angiotensin Converting Enzyme \n")
                f.write(" This gene encodes an enzyme involved in catalyzing the conversion of angiotensin I into a physiologically active peptide angiotensin II.Hence a reported increase in ACE serum levels can serve as an indicator for detection \n")
                f.write(" GRADE : 1 \n" )
                self.question = Label(text ="In which range do your serum ACE levels fall:", color =(0,0,0,1))
                self.add_widget(self.question)
                self.one = Label(text = "Serum levels less than 243 U/L", color =(0,0,0,1))
                self.add_widget(self.one)

                self.checkbox_one = CheckBox(color = (0,1,0,1), width=5,  background_checkbox_normal='black.jpg')
                self.checkbox_one.bind(active=on_checkbox_active_one)
                self.add_widget(self.checkbox_one)
                self.two = Label(text = "Serum levels between 243-336 U/L", color =(0,0,0,1))
                self.add_widget(self.two)
                self.checkbox_two = CheckBox(color = (1,0,0,1), width=5,  background_checkbox_normal='black.jpg')
                self.checkbox_two.bind(active=on_checkbox_active_two)
                self.add_widget(self.checkbox_two)
                self.three = Label(text = "Serum levels between greater than 336 U/L", color =(0,0,0,1))
                self.add_widget(self.three)
                self.checkbox_three = CheckBox(color = (1,0,0,1), width=5,  background_checkbox_normal='black.jpg')
                self.checkbox_three.bind(active=on_checkbox_active_three)
                self.add_widget(self.checkbox_three)




            f.write("\n\n GENE :"+ row["GENE SYMBOL"] +"-" + row["GENE NAME"]+ '\n')
            f.write(row["GENE DESC"]+ '\n')
            f.write(" P-value based Grade assigned: " +row["GRADE"]+ '\n' )


            for i in range(int(row['No_Of_Q'])):

                def on_checkbox_active_yes(checkbox_yes, value):
                    if value:
                        score_calc(1)


                def on_checkbox_active_no(checkbox_no, value):
                    if value:
                        score_calc(0)

                self.question = Label(text="Q" + str(i+1) + row['Q'+ str(i+1)], color =(0,0,0,1))
                self.add_widget(self.question)
                self.yes = Label(text = "YES", color =(0,0,0,1))
                self.add_widget(self.yes)

                self.checkbox_yes = CheckBox(color = (0,1,0,1), width=5,  background_checkbox_normal='black.jpg', group = 'ans' + str(i))
                self.checkbox_yes.bind(active=on_checkbox_active_yes)
                self.add_widget(self.checkbox_yes)
                self.no = Label(text = "No", color =(0,0,0,1))
                self.add_widget(self.no)
                self.checkbox_no = CheckBox(color = (1,0,0,1), width=5,  background_checkbox_normal='black.jpg', group= 'ans' + str(i))
                self.checkbox_no.bind(active=on_checkbox_active_no)
                self.add_widget(self.checkbox_no)




                def score_calc(param):
                    if param == 1:


                        self.total_score += float(row["SCORE_IF_YES_"+ str(i+1)]) * int(row["GRADE"])
                        self.score_dict[row['GENE SYMBOL']]= self.total_score


                    else:
                        self.total_score += float(row["SCORE_IF_NO_"+ str(i+1)]) *  int(row["GRADE"])
                        self.score_dict[row['GENE SYMBOL']]= self.total_score


                    print(self.total_score)

            #if count !=20:
            self.next = Button(text="Next")
            self.next.bind(on_press = self.next_button)
            self.add_widget(self.next)
            self.back = Button(text="Back")
            self.back.bind(on_press = self.back_button)
            self.add_widget(self.back)

    def back_button(self, instance):
        sm = detect_app.screen_manager.previous()
        detect_app.screen_manager.current = sm




    def next_button(self, instance):
        self.count+=1
        if self.count == 19:
            print(" being generated")
            with open("presults.txt", 'a') as f:
                f.write(" Total score thus calculated :" + str(self.total_score) + '\n')
                f.write("Gene wise score assigned BASED ON YOUR RESPONSES \n")
                for item in self.score_dict:
                    f.write(f" {item} -> {self.score_dict[item]} \n")
            self.clear_widgets()
            self. header = Label(text = "RESULTS", color = (0,0,0,1))
            self.add_widget(self.header)
            self.header1 = Label(text = "Congratulations on successfully completing the questionnaire", color = (0,0,0,1))
            self.add_widget(self.header1)
            self.header2 = Label(text =  "A detailed report has been generated as file \"presults.txt\"", color = (0,0,0,1))
            self.add_widget(self.header2)

            self.text = Label(text = f" Score obtained by you : {self.total_score}", color = (255,0,0,1))
            self.add_widget(self.text)
            self.weight = Label(text = " Weighting scheme used =  P-VALUE BASED GRADE ALLOCATION", color = (0,0,0,1))
            self.add_widget(self.weight)


            self.maximum = Label(text = " Maximum score possible = 36 ", color = (0,0,0,1))
            self.add_widget(self.maximum)
            self.ratio = Label(text = f" Rationalized  score(relative to maximum risk) = {self.total_score/36} ", color = (0,0,0,1))
            self.add_widget(self.ratio)

        else:
            self.display(self.count)




class StringInteractions(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (Window.size[0], self.size[1])
        self.cols = 1
        self.count = -1
        self.padding = [20,10,20,10]

        self.header =Label(text ="INTEGRATIVE NETWORK ANALYSIS", color =(0,0,0,1), size_hint_y = None)
        self.add_widget(self.header)
        self.text1 = Label(text= "You will be presented queries for each gene one by one.", color =(0,0,0,1), size_hint_y = None )

        self.add_widget(self.text1)
        self.centre = Image(source="network.png", size=(80,80))
        self.add_widget(self.centre)
        self.text2 = Label(text= "Select YES or NO for each question. The scores will be calculated accordingly", color =(0,0,0,1),  size_hint_y = None)
        self.add_widget(self.text2)

        self.next = Button(text="Next", size_hint_y=None)
        self.next.bind(on_press = self.next_button)
        self.add_widget(self.next)
        self.final_score =0


        self.gene_dict = {'ACE': 0, 'DPP4': 0, 'APOE': 0, 'VEGFA': 0, 'ADM': 0, 'CY2PC19': 0, 'CHN2': 0, 'XRCC1': 0, 'TNFRSF11B': 0, 'ADIPOQ': 0, 'CNR1': 0, 'AKR1B1': 0, 'ALDH2': 0, 'FTO': 0, 'CDKAL1': 0, 'API5': 0, 'ARHGAP22': 0, 'GSTT1': 0}
        self.score_dict = {'ACE': 0, 'DPP4': 0, 'APOE': 0, 'VEGFA': 0, 'ADM': 0, 'CY2PC19': 0, 'CHN2': 0, 'XRCC1': 0, 'TNFRSF11B': 0, 'ADIPOQ': 0, 'CNR1': 0, 'AKR1B1': 0, 'ALDH2': 0, 'FTO': 0, 'CDKAL1': 0, 'API5': 0, 'ARHGAP22': 0, 'GSTT1': 0}
        self.int_dict = {'ACE_DPP4': 2, 'ACE_APOE': 4, 'ACE_VEGFA':4, 'ACE_ADM': 2, 'ADIPOQ_CNR1':2, 'AKR1B1_ALDH2':16, 'CDKAL1_FTO':2}

        newn = f"""Diabetic Retinopathy Risk Score Report

                Method used for Weighing Scores : STRING INTERATIONS BETWEEN SELECT GENES

                The scores are first weighted by the degrees of freedom of each gene.
                Then according to the data available on interactions,  a certain multiplier is used for pairs of genes occuring together in a patient as follows :
                {self.int_dict}

                Details of genes and scoring scheme"""


        with open("stringresults.txt",'w') as f:
            f.truncate(0)
            f.write(newn)
    def final(self):

        print(self.int_dict)
        print(self.score_dict)
        print(self.gene_dict)
        for item in self.int_dict:

            x = item.split('_')
            if (self.gene_dict[x[0]]==1 and self.gene_dict[x[1]]==1):
                self.score_dict[x[0]]*=self.int_dict[item]
                self.score_dict[x[1]]*=self.int_dict[item]

        values = self.score_dict.values()
        self.final_score = sum(values)
        print(self.final_score)


    def display(self, count):
        self.clear_widgets()
        self.clear_widgets()
        self.count = count
        self.score =0

        self.total_score = 0



        with open('genedetails.csv', 'r') as csv_file, open('stringresults.txt', 'a') as f:

            self.csv_reader = csv.DictReader(csv_file)
            self.new_reader = list(self.csv_reader)
            row = self.new_reader[self.count]
            self.score =0
            self.total_score =0
            self.header =Label(text ="Query for :" + row["GENE SYMBOL"]+ "- " + row["GENE NAME"],color =(0,0,0,1))
            self.add_widget(self.header)


            def on_checkbox_active_one(checkbox_one, value):
                if value:
                    score_ACE(0)
            def on_checkbox_active_two(checkbox_two, value):
                if value:
                    score_ACE(0.5)
            def on_checkbox_active_three(checkbox_three, value):
                if value:
                    score_ACE(1)
            def score_ACE(param):
                self.score = param*4
                if param>=0.5:
                    self.score_dict['ACE']= self.score
                    self.gene_dict['ACE']=1

            def on_checkbox_active_yes(checkbox_yes, value):
                if value:
                    score_calc(self,1)
            def on_checkbox_active_no(checkbox_no, value):
                if value:
                    score_calc(self,0)
            def score_calc(self,param):
                if param == 1:
                    self.score += float(row["SCORE_IF_YES_"+ str(i+1)]) * int(row["DOF"])
                    self.score_dict[row['GENE SYMBOL']]= self.score
                    self.gene_dict[row['GENE SYMBOL']]=1

                else:
                    self.score += float(row["SCORE_IF_NO_"+ str(i+1)]) *  int(row["DOF"])
                    self.score_dict[row['GENE SYMBOL']]= self.score
                    self.gene_dict[row['GENE SYMBOL']]=0







            self.i = 0
            if(int(row['No_Of_Q'])==0):
                f.write("\n\n GENE :- ACE - Angiotensin Converting Enzyme \n")
                f.write(" This gene encodes an enzyme involved in catalyzing the conversion of angiotensin I into a physiologically active peptide angiotensin II.Hence a reported increase in ACE serum levels can serve as an indicator for detection \n")
                f.write(" DEGREES OF FREEDOM : 4 \n" )
                self.question = Label(text ="In which range do your serum ACE levels fall:", color =(0,0,0,1))
                self.add_widget(self.question)
                self.one = Label(text = "Serum levels less than 243 U/L", color =(0,0,0,1))
                self.add_widget(self.one)

                self.checkbox_one = CheckBox(color = (0,1,0,1), width=5,  background_checkbox_normal='black.jpg')
                self.checkbox_one.bind(active=on_checkbox_active_one)
                self.add_widget(self.checkbox_one)
                self.two = Label(text = "Serum levels between 243-336 U/L", color =(0,0,0,1))
                self.add_widget(self.two)
                self.checkbox_two = CheckBox(color = (1,0,0,1), width=5,  background_checkbox_normal='black.jpg')
                self.checkbox_two.bind(active=on_checkbox_active_two)
                self.add_widget(self.checkbox_two)
                self.three = Label(text = "Serum levels between greater than 336 U/L", color =(0,0,0,1))
                self.add_widget(self.three)
                self.checkbox_three = CheckBox(color = (1,0,0,1), width=5,  background_checkbox_normal='black.jpg')
                self.checkbox_three.bind(active=on_checkbox_active_three)
                self.add_widget(self.checkbox_three)


            f.write("\n\n GENE :"+ row["GENE SYMBOL"] +"-" + row["GENE NAME"]+ '\n')
            f.write(row["GENE DESC"]+ '\n')
            f.write(" DEGREES OF FREEDOM: " +row["DOF"]+ '\n' )



            for i in range(int(row['No_Of_Q'])):


                self.question = Label(text="Q" + str(i+1) + row['Q'+ str(i+1)], color =(0,0,0,1))
                self.add_widget(self.question)
                self.yes = Label(text = "YES", color =(0,0,0,1))
                self.add_widget(self.yes)

                self.checkbox_yes = CheckBox(color = (1,1,1,1), width=5)
                self.checkbox_yes.group = 'ans' + str(i)
                self.checkbox_yes.bind(active=on_checkbox_active_yes)
                self.add_widget(self.checkbox_yes)

                self.no = Label(text = "NO", color =(0,0,0,1))
                self.add_widget(self.no)
                self.checkbox_no = CheckBox(color = (1,1,1,1), width=5)
                self.checkbox_no.group = 'ans' + str(i)
                self.checkbox_no.bind(active=on_checkbox_active_no)
                self.add_widget(self.checkbox_no)







            self.next = Button(text="Next")
            self.next.bind(on_press = self.next_button)
            self.add_widget(self.next)

            self.back = Button(text="Back")
            self.back.bind(on_press = self.back_button)
            self.add_widget(self.back)


    def back_button(self, instance):

        detect_app.screen_manager.current = "Menu"




    def next_button(self, instance):
        self.count+=1

        if self.count == 19:
            print("Report being generated")
            self.final()
            with open("stringresults.txt", 'a') as f:
                f.write(" Total score thus calculated :" + str(self.final_score))
                f.write("Gene wise score assigned BASED ON YOUR RESPONSES")
                for item in self.score_dict:
                    f.write(f" {item} -> {self.score_dict[item]} \n")
            self.clear_widgets()
            self.header = Label(text = "RESULTS", color = (0,0,0,1))
            self.add_widget(self.header)
            self.header1 = Label(text = "Congratulations on successfully completing the questionnaire", color = (0,0,0,1))
            self.add_widget(self.header1)
            self.header2 = Label(text =  "A detailed report has been generated as file \"stringresults.txt\"", color = (0,0,0,1))
            self.add_widget(self.header2)
            self.text = Label(text = f" Score obtained by you : {self.final_score}", color = (255,0,0,1))
            self.add_widget(self.text)
            self.weight = Label(text = " Weighting scheme used =  STRING INTERACTIONS BETWEEN SELECT GENES", color = (0,0,0,1))
            self.add_widget(self.weight)

            self.maximum = Label(text = " Maximum score possible = 306 ", color = (0,0,0,1))
            self.add_widget(self.maximum)
            self.ratio = Label(text = f" Rationalized  score(relative to maximum risk) = {self.final_score/306} ", color = (0,0,0,1))
            self.add_widget(self.ratio)

        else:
            self.display(self.count)

class DetectApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.main_page = MainPage()
        screen = Screen(name="Main")
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)

        self.page = Page()
        screen = Screen(name="Menu")
        screen.add_widget(self.page)
        self.screen_manager.add_widget(screen)


        self.pvalue = P_Value()
        screen = Screen(name="P_Value")
        screen.add_widget(self.pvalue)
        self.screen_manager.add_widget(screen)


        self.string = StringInteractions()
        screen = Screen(name="String")
        screen.add_widget(self.string)
        self.screen_manager.add_widget(screen)


        return self.screen_manager

if __name__ == "__main__":

    detect_app = DetectApp()
    detect_app.run()
