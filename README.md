#randJapGenerator
This small python program can help you memorize _Japanese characters(Hiragana, Katagana)_.
It generate a dictation sheet tells you the Roma reading, and you have to dictate the corresponding character yourself.
All the characters are arranged in random order. 
You can even modify the csv file to generate the dictation sheet based on your needs. 

## Installation
Clone the github repository and use python 2.7 to compile it. 
```
git clone https://github.com/whitefusion/randJapGenerator.git
python rand50GenMain.py JapSyllabary.csv
```
Then you should get two pdfs "dictation.pdf" and "solution.pdf" in your working directory.

## Necessary Modules 
* Python Image Library(PIL)
* skimage
* matplotlib
* numpy



