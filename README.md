[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Diabetic-Retinopathy-Risk-Prediction

The current project aims to deliver a probabilistic score based on the genetic information entered by the patient pertaining to selected genes. DetectRetino, the GUI based software developed as an outcome of this project combines all the skills and techniques learnt in my practice school(CSIR-Institute of Genomics and Integrative Biology), so far to deliver the same objective. The user-interface is designed in such a way that the user only needs to enter select information and fill in few multiple-choice questions per gene pertaining to allele type, SNP polymorphisms, ethnicity, gender and lifestyle habits. The program based on the algorithm then calculates a risk score automatically indicating the probability of the patients having Diabetic Retinopathy.

DetectRetino has been developed as a Desktop App completely using Python and Kivy.

The dictionary of questions prepared by us and the corresponding raw unweighted scoring scheme can be found in Diabetic Retinopathy Detection.docx file.
# Dependencies
* Python==3.7.1
* Kivy==1.11.1

# Getting Started
With some basic steps to follow, you can easily run the software on your PC/Laptop:
# Installation:
* Fork this repositiory to your github account.
* Clone the repo
   ```sh
   git clone https://github.com/[your-github-user-account]/Diabetic-Retinopathy-Risk-Prediction.git
   ```
*  Run the following sequence of commands:
   ```sh
   cd Diabetic-Retinopathy-Risk-Prediction
   python3 GUI.py
   ```
* A window as shown below appears, asking you to enter the patient name and the patient ID:

  
  

# References :


•	Rani, J., Mittal, I., Pramanik, A., Singh, N., Dube, N., Sharma, S., … Ramachandran, 
S. (2017). T2DiACoD: A Gene Atlas of Type 2 Diabetes Mellitus Associated 
Complex Disorders. Scientific Reports, 7(1). doi: 10.1038/s41598-017-07238-0 

•	 T2DiACoD: Gene Atlas. (n.d.). Retrieved from http://t2diacod.igib.res.in

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/thecodeeagle/Diabetic-Retinopathy-Risk-Prediction/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ashlesha-kumar-bitsp/
