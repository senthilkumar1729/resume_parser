# Resume parser

Simple web-app made with streamlit that parses a resume to retreive a list of candidate "skills". 

I primarly built this to play with Spacy's entity-ruler which allows you to build a rule based NER model. The ruler uses patterns provided in the temp.jsonl dataset.


## Requirement

- Streamlit
- Spacy
- NLTK
- Textract


## Usage

Clone it!

```
$ git clone https://github.com/senthilkumar1729/resume_parser.git
```


Go into the project directory and run the command:

```
$ streamlit run streamlit_app.py
```

Open `http://localhost:8501` and upload a pdf that needs parsing!

## Web-app

![resume](https://user-images.githubusercontent.com/20635881/207072786-cdf596cb-d6e7-4f44-b823-7512cfb590f3.png)


Upload your pdf and click on 'Get Skills' 

![skillls](https://user-images.githubusercontent.com/20635881/207072980-53780e35-ad7f-43a3-896f-52e6e08fa3c7.png)

The webpage should return a list of skills!
