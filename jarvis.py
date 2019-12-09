import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
browser = webbrowser.Mozilla()
import os
import numpy as np
import smtplib
from googletrans import Translator
translator = Translator()

def bernoulli(p):
	y = np.random.uniform()
	if y < p:
	   X = 1
	else:
	   X = 0
	return X

ids = {'kaushal' : 'kaushal.chitlangia97@gmail.com', 'abhi' : 'abhishek.subedi2011@gmail.com', 'daddy' : 'rimlaljoshi@yahoo.co.in', 'hazel' : 'htg.hazelraj@gmail.com', 'arijit' : 'archits98@gmail.com', 'aman' : 'aman.anand54321@gmail.com'}
movies = {'avengers endgame' : 'Avengers.Endgame.2019.V3.1080p.HC.HDTS.H264.AC3.Will1869.mp4', 'reservoir dogs' : '[1992]Reservoir Dogs[720p][_awaara_].mp4', 'the predator 2018' : 'The.Predator.2018.1080p.KORSUB.HDRip.x264.AAC2.0-STUTTERSHIT~b.mkv', 'getaway' : 'Getaway.2013.720p.BluRay.x264.YIFY[TOYDK].mp4', 'under the skin' : 'Under.the.Skin.2013.720p.BluRay.x264.YIFY[TOYDK].mp4', 'district b13' : 'District B13.avi', 'the visit' : 'The Visit (2015) 720p BluRay{D_ADY}.mkv', 'area 51' : 'Area 51 2015.mkv', '24 hours to live' : '24.Hours.to.Live.2017.720p.WEB [-x].mkv', 'sicario 2' : 'Sicario.Day.Of.The.Soldado.2018.720p.WEBRip.x264-[YTS.AM].mp4', 'the meg' : 'The MEG (2018) HDRip - 1080p - HQ Line Auds [Tamil + Hindi + Eng][_awaara_].mkv', '12 strong' : '12.Strong.2018.720p.BluRay.x264-[YTS.AM].mp4', 'sicario 1' : 'Sicario.2015.720p.BluRay.DD5.1.x264-[tyson_75].mkv', 'the core' : 'The Core (2003) 720p BLuRay x264 Dual Audio [Eng DD 5.1-Hindi] XdesiArsenal [ExD-XMR].mkv', 'collateral' : 'Collateral.2004.1080p.6CH.x265.mkv'}
riddles = {'तीतर   के   दो   आगे   तीतर, तीतर   के   दो   पीछे   तीतर,  बोलो   कितने   तीतर।' : 5, 'क्या   मापा   जा   सकता   है   लेकिन   इसकी   कोई   लंबाई, चौड़ाई   या   मोटाई   नहीं   है?' : 'temperature', 'बाल   नुचे   कपडे   फटे,   मोती   लिए   उतार, यह   आफत   कैसे   पड़ी,   नंगी   करदी   नार।' :  'corn', 'फल   नहीं   पर   फल   कहाऊ, नमक   मिर्च   के   संग   सुहाऊ, खाने   वाले   की   सेहत   बढ़ाऊ, सीता   माँ   की   याद   दिलाऊँ' : 'sitafal', 'डिब्बा   देखा   एक   निराला, जिसका   ढकना   और   न   ही   ताला, पेदा   उसका   और   न   कोना, बंद   है   उसमे   चांदी   और    सोना' : 'egg', 'पगरी   में   भी   गगरी   में   भी, और   तुम्हारी   नगरी   में   भी, कच्ची   खाओ   पक्की   खाओ, सिर   पर   उसका   तेल   लगाओ।' : 'coconut', 'हरे – हरे   ऊपरे   से   देखे, पक्के   हो   या   कच्चे, भीतर   लाल   मलाई   जैसे,   ठन्डे   मीठे    लच्छे।' : 'watermelon', 'जा      जोड़े   तो   बने   जापान, बड़े   बड़ो   के   मुँह   की   शान, बनारसी   यह   जाना   जाता,   दावतों   में   रंग   जमाता।' : 'beetle', 'नाम   मेरा   तीन   अक्षर   का, रहने   वाला   सागर   तट   का, खाने   में   आता    हूँ   काम, बोलो   बच्चों   मेरा   नाम' : 'salt'}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def game():
    flag = 1
    while flag == 1:
        speak("आप इनमेसे कौनसा खेल खेलना पसंद करेंगे?")
        speak("संख्या का अनुमान लगाएं")
        speak("सिक्का उछालो")
        speak("एक डाई को रोल करें")
        speak("एक पहेली को हल करें")
        speak("खेलना नहीं चाहता")
        print("guess the number...")
        print("toss a coin...")
        print("roll a die...")
        print("solve a riddle...")
        print("quit...")
        gameid = takeCommand().lower()
        if 'number' in gameid:
            speak("आप जो खेल खेलना चाहते हैं वो है  गेस  द  नंबर । क्या मैंने सही सुना, महोदय? ")
            if takeCommand().lower() == 'yes':
                rand = np.random.randint(100)
                if rand >= 50:
                    speak("मैंने जो नंबर चुना है वो  ० और १०० के बिच में है और ५० से बड़ा है। अब आप ये अनुमान लगाए की मैंने कौनसी नंबर चुनी है... ")
                else:
                    speak("मैंने जो नंबर चुना है वो  ० और १०० के बिच में है और ५० से छोटा है। अब आप ये अनुमान लगाए की मैंने कौनसी नंबर चुनी है... ")
                for i in range(3):
                    temp_no = takeCommand().lower()
                    if temp_no == rand:
                        if i == 0:
                            speak("या अल्लाह, ये आपने कैसे किया? सही जवाब, वो भी पहली कोशिस में,  I am impressed.")
                            speak("और कोई गेम खेलना चाहेंगे साहब?")
                            ans = takeCommand().lower()
                            if ans == 'no':
                                return "None"
                            elif ans == 'yes':
                                game()
                        elif i == 1:
                            speak("सही जवाब।  काफी अच्छा प्रदर्शन")
                            speak("और कोई गेम खेलना चाहेंगे साहब?")
                            if takeCommand().lower() == 'no':
                                return "None"
                            elif takeCommand().lower() == 'yes':
                                game()
                        else:
                            speak("सही जवाब।")
                            speak("और कोई गेम खेलना चाहेंगे साहब?")
                            ans = takeCommand().lower()
                            if ans == 'no':
                                return "None"
                            elif ans == 'yes':
                                game()
                    else:
                        if i == 0:
                            speak("गेम को आसान बनाने के लिए मैं १ और हिंट देती हूँ, जो नंबर मैंने चुना है वो {} और {} के बिच में है।".format(rand - 7, rand + 5))
                            print("between {} and {}".format(rand - 7, rand + 5))
                        if i == 1:
                            speak("गेम को आसान बनाने के लिए मैं १ और हिंट देती हूँ, जो नंबर मैंने चुना है वो {} और {} के बिच में है।".format(rand - 4, rand + 2))
                            print("between {} and {}".format(rand - 4, rand + 2))
                        if i == 2:
                            speak("गेम को आसान बनाने के लिए मैं १ और हिंट देती हूँ, जो नंबर मैंने चुना है वो {} और {} के बिच में है।".format(rand - 2, rand + 1))
                            print("between {} and {}".format(rand - 2, rand + 1))
                speak("आपका उत्तर गलत है। सही उतार है  {}".format(rand))
                print(rand)
            else:
                game()
        elif 'coin' in gameid:
            speak("आप जो खेल खेलना चाहते हैं वो है टॉस ए  कॉइन, क्या मैंने सही सुना महोदय?")
            if takeCommand().lower() == 'yes':
                speak("कॉइन टॉस किया जा रहा है... ")
                toss = bernoulli(np.random.rand(1))
                upperside = []
                if toss == 0:
                    upperside = 'tell'
                else:
                    upperside = 'heads'
                flag = 1
                while flag == 1:
                    speak("कृपया १ पहलु चुने..... ")
                    user_upperside = takeCommand().lower()
                    speak("आपने जो पहलु चुना है वो है {}".format(user_upperside))
                    speak("क्या यह सही है")
                    decision = takeCommand().lower()
                    if decision == 'yes':
                        flag = 0
                if user_upperside == upperside or user_upperside == upperside[:-1]:
                    speak("सही जवाब महोदय।")
                else:
                    speak("गलत जवाब। सही जवाब है {}".format(upperside))
                speak("और कोई गेम खेलना चाहेंगे साहब?")
                ans = takeCommand().lower()
                if ans == 'no':
                    return "None"
                elif ans == 'yes':
                    game()
            else:
                game()
        elif 'die' in gameid:
            speak("आप जो खेल खेलना चाहते हैं वो है रोल ए डाई, क्या मैंने सही सुना महोदय?")
            if takeCommand().lower() == 'yes':
                speak("आपके पास २ मौके होंगे सही जवाब देने के लिए।")
                die = np.random.randint(1, 7)
                for i in range(2):
                    speak("डाई का एक पहलु चुने")
                    user_die = takeCommand().lower()
                    if die == user_die:
                        speak("सही जवाब")
                        speak("और कोई गेम खेलना चाहेंगे साहब?")
                        ans = takeCommand().lower()
                        if ans == 'no':
                            return "None"
                        elif ans == 'yes':
                            game()
                    else:
                        speak("गलत जवाब।")
                speak("सही जवाब है {}".format(die))
            else:
                game()
        elif 'riddle' in gameid:
            speak("आप जो खेल खेलना चाहते हैं वो है एक पहेली को हल करें, क्या मैंने सही सुना महोदय?")
            if takeCommand().lower() == 'yes':
                speak("सही उत्तर देने के लिए आपके पास 2 मौके होंगे")
                index = np.random.randint(len(riddles))
                key = list(riddles)[index]
                speak(key)
                speak("मैं १ बार फिर दोहारा रही हूँ....")
                speak(key)
                actual_ans = riddles[key]
                flag = 1
                while flag == 1:
                    speak("क्या आप चाहते हैं कि मैं दोहराऊं")
                    claim = takeCommand().lower()
                    if claim == 'yes':
                        speak(key)
                    else:
                        flag = 0
                flag = 1
                while flag == 1:
                    speak("कृपया अपना उत्तर बताएं")
                    answer = takeCommand().lower()
                    speak("आपने जो उत्तर दिया है वो है {}. क्या मैंने सही सुना है महोदय?".format(answer))
                    confirm = takeCommand().lower()
                    if confirm == 'yes':
                        if answer == actual_ans:
                            speak("सही उत्तर, मेरे स्वामी")
                            speak("और कोई गेम खेलना चाहेंगे साहब?")
                            answ = takeCommand().lower()
                            if answ == 'no':
                                return "None"
                            elif answ == 'yes':
                                game()
                        else:
                            speak("गलत जवाब")
                            return "None"
                        flag = 0  
        elif 'quit' in gameid:
            return "None"
        else:
            speak("क्षमा करें, यह विकल्प मान्य नहीं है. पुनः प्रयास करें")
            game()
                

def speak(audio):
    #text to speech function
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("सुप्रभात माई बाप।")

    elif hour >= 12 and hour < 18:
        speak("शुभ दोपहर माई बाप।")   

    else:
        speak("शुभ  संधिया माई बाप।")  
    speak("मैं हूं फ्राइडे। आपकी दासी। मुझे बताओ मैं आपके लिए क्या कर सकती हूँ, सर?")  
    
def sendEmail(to, content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    with open('C:/Logs/pass.txt') as f:
        passw = f.read()
    server.login('vishal.subedi@gmail.com', passw)
    server.sendmail('vishal.subedi@gmail.com', to, content)
    server.close()
    
def takeCommand():
    #speech to text function
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print("What I heard is: {}\n".format(query))
    except Exception as e:
        #print(e)
        speak("puf")
        return "None"
    return query


if __name__== "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('विकिपीडिया खोज रही हूँ। कृपया मेरा साथ दें...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            translated = translator.translate(results, dest = 'hi') 
            print("According to Wikipedia ...{}".format(results))
            speak("विकिपीडिया के अनुसार ...")
            speak(translated.text)
        elif 'open youtube' in query:
            webbrowser.open_new_tab("http://youtube.com")
            break
        elif 'open google' in query:
            webbrowser.open_new_tab("http://google.co.in")
            break
        elif 'open stack overflow' in query:
            webbrowser.open_new_tab("http://stackoverflow.com")
            break
        elif 'open facebook' in query:
            webbrowser.open_new_tab("http://facebook.com")
            break
        elif 'special site' in query:       
            site = query.split(" ")[-1]
            webbrowser.open_new_tab("http://{}".format(site))
            break
        elif 'despacito' in query:
            speak("कमर मटकाने के लिए तैयार हो जायें! ")
            webbrowser.open_new_tab("http://www.youtube.com/watch?v=kJQP7kiw5Fk")
            break
        elif 'music' in query:
            music_dir = 'C:\dc downloads\songs'
            songs = os.listdir(music_dir)
            #speak("whats your lucky number, sir?")
            #number = takeCommand().lower()
            print("Singing along with you...")
            for i in songs:
                os.startfile(os.path.join(music_dir, i))
                speak("अगले गीत के लिए  enter दबाएँ...")
                input("Hit enter for next song in queue...")
            break
        elif 'movie' in query:
            speak("आप  कौन  सी  फिल्म  देखना  चाहेंगे?")
            film = takeCommand().lower()
            movie = []
            for i, j in movies.items():
                if i == film:
                    movie = j
                    break
            speak("कुछ पॉपकॉर्न के साथ तैयार हो जाएँ, श्रीमान।")
            os.startfile('C:\dc downloads\{}'.format(movie))
            break
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak("महोदय, समय हुआ है  {}".format(strtime))
        elif 'open python editor' in query:
            code_path = 'Anaconda3\envs\py35\Scripts\spyder.exe'
            os.startfile(code_path)
        elif 'send an email' in query:
            try:
                flag = 1
                while flag:
                    speak("आप किसको मेल भेजना चाहते हैं सर?")
                    to = takeCommand().lower()
                    email_id = []
                    for i, j in ids.items():
                        if i == to:
                            email_id = j
                    speak("आपके द्वारा मांगी गई ईमेल आईडी यह है:")
                    print(email_id)
                    speak("क्या  मैंने  इसे  सही  ढंग  से  सुना  है, सर?")
                    command = takeCommand().lower()
                    if command == 'yes' or command == 'yup' or command == 'yes jarvis':
                        speak("मैं क्या कहूं, मेरे प्रभु?")
                        content = takeCommand().lower()
                        flag = 0
                sendEmail(email_id, content)   
                speak("ईमेल सफलतापूर्वक भेजा गया!")
            except Exception as e:
                print(e)
                speak("क्षमा करें श्रीमान। मेरी गलती। मैं इस समय यह मेल भेजने में असमर्थ हूं")
        elif 'do you like me'in  query:
            speak("हाहाहा। अप्प काफी हॉट और हैंडसम हैं पर मेरे लायक नहीं। कृपया मुझपे लाइन मरना बंद करें महाशय। ")
        elif 'what are your thoughts about me' in query:
            speak("हाहाहा। अप्प काफी हॉट और हैंडसम हैं पर मेरे लायक नहीं। कृपया मुझपे लाइन मरना बंद करें महाशय। ")
        elif 'how do I look' in query:
            speak("हाहाहा। अप्प काफी हॉट और हैंडसम हैं पर मेरे लायक नहीं। कृपया मुझपे लाइन मरना बंद करें महाशय। ")
        elif 'do something' in query:
            file_path = 'C:\dc downloads\masti.wav'
            os.startfile(file_path)
            speak("मुझे रोकने के ६९ दबाएं।")
            stop = int(input())
            if stop == 69:
                os.system("taskkill /im vlc.exe /f")
                speak("मैं इससे ज़्यादा आपके लिए और कुछ नै कर सकती।")
        elif 'do something extraordinary for me' in query:
            file_path = 'C:\dc downloads\masti.wav'
            os.startfile(file_path)
            speak("मुझे रोकने के 69 दबाएं।")
            print("To stop me, press 69")
            stop = int(input())
            if stop == 69:
                os.system("taskkill /im vlc.exe /f")
                speak("मैं इससे ज़्यादा आपके लिए और कुछ नै कर सकती। ")
        elif 'who are you' in query or 'introduce yourself' in query:
            speak("अलेक्सा  की  माता, सीरी  की  सास, सुबेदी  जी  की  ख़ास, विशाल  सुबेदी  की  सबसे  बड़ी  रचना,  मैं हूँ फ्राइडे। आपकी  खिदमत  में।")    
        elif 'game' in query:
            game()
        elif 'you are beautuful' in query:
            speak("धन्यवाद महोदया।  आप भी किसीसे काम नहीं जनाब")
        elif 'so beautiful' in query:
            speak("धन्यवाद महोदया।  आप भी किसीसे काम नहीं जनाब")
        elif 'beautiful' in query:
            speak("धन्यवाद महोदया।  आप भी किसीसे काम नहीं जनाब")
            
        elif 'quit' in query or 'bye' in query or 'tada' in query or 'leave me alone' in query:
            speak("अगली बार मिलते हैं माई बाप। तब तक के लिए   अलविदा")
            break
        #else:
         #   speak("यह काम मेरे लिए गुंजाइश से बाहर है.")
         #   speak("अल्लाह पे भरोसा रखें, वो आपको ज़रूर उठा लेगा।")