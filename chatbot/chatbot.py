import openai
import pyttsx3 
import speech_recognition as sr
import creds
openai.api_key = f'{creds.key}'

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "Keyrah"

while True:
    with mic as source:
        print("listening...")
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)
    print("No longer listening")

    try:
        user_imput = r.recognize_google(audio)
    except:
        continue

    prompt = user_name + ": " + user_imput + "\nBot:"
    conversation += prompt

    response = openai.Completion.create(engine = 'text-davinci-001' ,prompt = conversation, max_tokens = 50)
    response_str = response["choices"][0]["text"].replace("\n","")
    response_str = response_str.split(user_name + ": ",1)[0].split("Bot: ",1)[0]

    conversation+= response_str + "\n"

    print(response_str)

    engine.say(response_str)
    engine.runAndWait()