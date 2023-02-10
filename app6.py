#quiz program
from logging import logMultiprocessing


quiz={
    'question1':{
        'question':'what is the worst moment in your life?',
        'answer':'losing important people'
    },
    'question2':{
        'question':'what is the largest river in world?',
        'answer':'River NIle'
    },
    'question3':{
        'question':'what is the capital city of Kenya?',
        'answer':'Nairobi'
    },
    'question4':{
        'question':'what is the  capital of southafrica?',
        'answer':'pretoria'
    },
    'question5':{
        'question':'what is the largest river in kenya',
        'answer':'River Tana'
    },
    'question6':{
        'question':'what is the largest Lake in world?',
        'answer':'Lake victoria'
    },
    'question7':{
        'question':'what is the highest mountain in world?',
        'answer':'kiimanjaro'
    },
     
    }


score=0


for key, value in quiz.items():
    print(value['question'])
    answer=input('Answer?')
    
    if answer.lower()==value['answer'].lower():
        print('Correct')
        score=score+1
        print('your score is:'+str(score))
        print('')
        print('')
        
        
    else:
        print('wrong!')
        print('The answer is :'+value['answer'])
        print('your score is:'+str(score))  
        print('')
        print('')
        
        
        
        
print('You got '+str(score)+'out of 7 questions correctly')
print('your percentage is '+str(int(score/7*100))+'%')          
