# Assignment 2 for Data Privacy and Security.

1 Laplace Mechanism 

Tasks:

(a) Derive the global sensitivity for the query (average age). 

Solution: For the average age query on the dataset, the global sensitivity (GSf) will be Maximum change in 
average age, when a single individual’s record is added or removed. Mathematically, it will be 

∆ f = Max Age – Min Age / n 

Where,

➢ n = Total number of Individual’s with age greater than 25.

➢ Max Age = 90 

How did we get to know that Maximum Age is 90? 

Maximum Age:

![image](https://github.com/user-attachments/assets/a594e806-2ad4-41ce-9f53-d309709876fe)

➢ We wrote a code, where we loaded the dataset to determine the Maximum Age.

Output Terminal: 

![image](https://github.com/user-attachments/assets/def43bc4-cd89-4ce6-a2a4-9a0b36e78f15)

➢ And we got Maximum Age as 90. 

➢ Now, as we have got Maximum Age as 90, we proceeded to calculate Global Sensitivity. 

Global Sensitivity: 

![image](https://github.com/user-attachments/assets/4e5c6f8b-6262-41f2-b7ce-14dca79e0131)

Output Terminal: 

![image](https://github.com/user-attachments/assets/548d8044-5062-40f3-9dc0-6d502b29cc82)

➢ we got Global Sensitivity as “0.002447418738049713” 

Note: 

➢ When GSf  is smaller, less noise is added to the dataset to achieve desired level of privacy. 

➢ When GSf is larger, more noise is added to the dataset to achieve desired level of privacy. 

(b) Calculate the variance for the Laplace noise and inject noise into the average age query result with 
0.5-differential privacy and 1-differential privacy, respectively 

Solution: To make dataset differentially private, we add Laplace noise to the query of result.

➢ Differential privacy is a framework which guarantees privacy, and handles, analyzes sensitive 
data. 

➢ Differential privacy system contains:  

➢ A database containing sensitive information. 

➢ Then Differential privacy mechanism/algorithm adds “noise” to the actual output of the query. 

➢ To understand it in a better way let’s say we want to release a database, containing, Number of 
employees who have certain health condition, let’s say database has 10 employees.

➢ We then use Laplace mechanism, which adds noise from Laplace distribution. Assume, we add a 
noise of +3. 

➢ Released Count is 10 + 3 = 13 

➢ Therefore, adversary cannot say whether the real count is 10,13 or any other number close to 13. 

➢ It’s the noise that makes the exact count of employees, uncertain, protecting privacy of 
individuals. 

![image](https://github.com/user-attachments/assets/0320503b-17c3-473a-8212-2de8e8235328)

Output:

➢ We got number of Individuals over 25 years in the dataset as 26150. 

➢ Original Avg age is 42.782256214149136 years. 

➢ And We calculated global sensitivity considering maximum age from dataset 90 and minimum age 
considered due to requirement at 26, as 0.002447418738049713. 

For noise injection and Variance calculations: 

➢ For ε = 0.5 – differential Privacy 

• b = ∆f/ε [Scale of Laplace distribution] 

• b0.5 = 0.004894837476099426. 

• Variance of the Laplace noise: 2b2 = 2*(0.004894837476099426)2 = 4.7918867834854805e
05 

• Noisy Average Age: 42.78272457906302 years, slightly higher than the original Avg age due 
to added noise. 

• Difference from Original Average Age: 0.0004683649138854662 years, represents the very 
minimal impact of noise on the average age, which maintains utility while enhancing 
privacy.

➢ For ε = 1.0 – differential Privacy 

• b = ∆f/ε [Scale of Laplace distribution] 

• b1.0 = 0.002447418738049713. 

• Variance of the Laplace noise: 2b2 = 2*(0.002447418738049713)2 = 1.1979716958713701e
05 

• Noisy Average Age: 42.78366535052656 years, slightly higher than the original Avg age due 
to added noise.

• Difference from Original Average Age: 0.0014091363774255683 years, showcases a slightly 
larger impact due to the nature of the noise, yet still preserving the query's utility.

2 Exponential Mechanism 

➢ It is a fundamental tool in differential privacy for releasing noisy but private outputs from sensitive 
data. 

➢ By selecting outputs from a set of possible outputs in a way that balances the utility of the output 
with privacy of individual whose data is being analyzed. 

➢ It works as assigning the scores to the potential outputs and sampling an output based on scores 
in a way that protects individuals’ privacy. 

➢ Exponential mechanism introduces randomness, this randomness, even with the low utility score, 
have non-zero chances of being selected, therefore we can say that it provides a level of privacy 
protection. 

Tasks: 

(a) Derive the global sensitivity for the query (most frequent” Education”) 

Solution: The global sensitivity for the most frequent “Education” level query is 1.  

➢ To understand, let’s say ‘HS-grad’ is the most frequent education level. 

➢ And if we add a record of an individual whose education level is ‘HS-grad’, the frequency of HS
grad will increase by 1. 

➢ In the same way, if we remove a record from ‘HS-grad’, its frequency will decrease by 1. 

➢ No matter how many records are in the dataset or how the frequencies are distributed, the 
maximum impact one record can have on the outcome of our query is change of one in the 
frequency count. 

➢ Therefore, global sensitivity for our query is 1.

(b) Compute the probabilities and generate the noisy output result with 0.5-differential privacy and 1- 
differential privacy, respectively 

Solution: 

![image](https://github.com/user-attachments/assets/8cc2a20b-2dc3-4a48-8250-1efdc04b327f)

Output:

![image](https://github.com/user-attachments/assets/a881efbc-98fd-4700-9814-7dcb1f18cc92)

![image](https://github.com/user-attachments/assets/9b7868bf-1017-4607-9e30-06bce728d167)

➢ We first loaded the dataset and calculated the frequency of each ‘Education’ Level. By doing this 
we understood the base utility of each education level, here we are still not thinking about privacy. 

➢ Then we found out Utility Score, Utility of each education level is defined by its frequency in the 
dataset. 

➢ The exponential mechanism is then applied to select an educational level based on their 
frequencies adjusted by the privacy parameter ε. 

➢ The mechanism randomly selects an educational level according to these probabilities.

For ε = 0.5, 
➢ We can see, HS-Grad has the highest probability in the distribution, yet we got selected “1st – 4th” 
Educational Level it’s because randomness (added noise) got introduced to protect the privacy. 

![image](https://github.com/user-attachments/assets/4462c246-882f-4b41-b6b3-b7fbc5c381d4)


For ε = 1.0, 

➢ We can see, HS-grad has the highest probability in the distribution, yet we got selected 
“Doctorate” Education Level it’s because randomness (added noise) got introduced to protect the 
privacy.

![image](https://github.com/user-attachments/assets/5d663e84-f27f-48ca-b035-673e9db60218)

![image](https://github.com/user-attachments/assets/8dad7385-a329-4c14-8ae4-3bd0fcb620dc)


