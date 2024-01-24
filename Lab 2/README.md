# 180DA-WarmUp-Lab-2

1. 
![Alt text](<subscriber-publisher interaction.png>)

• Consider how to use MQTT for the project. Based on your experiences, what is made possible us-
ing MQTT? What seems fairly difficult using MQTT? If you were to use MQTT, what would be a
reasonable communications lag time be? Would you prefer to use a different method of transmitting
data?

    MQTT allows for IoT devices to quickly and easily communicate with one another without have to
    establish a direct communication channel. It is easily scalable as it follows a publisher/subscriber
    model and also allows for asynchronous communication. Due to its asynchronous nature, MQTT struggles
    with strict ordering in message scheduling as well as extremely strict real time systems (its latency
    is typically fairly minute, however for extreme cases it could cause issues). A reasonable communication
    lag time for MQTT would be a few milliseconds given that the network it is connected to has a fairly low
    latency. Depending on our choice of project, MQTT could be a good choice for transmitting data in the case
    of something like a game controller where we have several buttons or sensor data that we need to transmit
    at the same time.

2. 
![Alt text](<speech recognition testing.png>)

• Try more similar sounding words (particularly bad examples may be words like “sound” and
“found”, letters (A, B, C , D, E , F, G). Does the performance start taking a hit?

    Performance begins taking a hit when vocalizing similar sounding words in quick sucession. As
    noted in the image above.

• Phrases. How long of a phrase can work? Is the length of a phrase actually a good thing for
“error correction”?

    It doesn't seem like there is a limit to the length of the audio sample for the Google speech
    recognition module I'm using. However I don't see too much of an increase or decrease in accuracy.
    Theoretically the longer a phrase or audio, sample the better it is for error correction however,
    due to the fact that the program can use semantic context clues from other recognized phrases and
    words to correct misheard words.

• Play music in the background. Go to a coffee shop (or work in the lab). How well does it work in
noise? What are ways to improve its performance in noise?

    Slight background music doesn't seem to interfere much but as the volume increases, evidently the
    speech recognition begins to struggle more and more. Some ways to improve the systems performance
    in noise could be to add a specific microphone that a user can talk into, use DSP principles that
    we learned to filter out noise and isolate the main speech, adjust sensitivity in our microphone,
    or look for models pretrained for noisy environments.

Write some short bullet points with some individual thoughts on how this applies to your project:
(a) What can you do with your given speech program in the project?

    For our project there's numerous applications for speech recognition and processing. Some
    possibilities include: voice user interfaces, karaoke, short commands (power ups, reload, etc.),
    character controls, real time translation, etc.

(b) How complex do you want your speech recognition to be? How complex can you reasonably expect
your speech recognition to be?

    Realistically I wouldn't want an overly complex speech recognition system. I would want its
    application in our project to be convenient, and straightforward, allowing it to improve over
    a traditionally hands on feature.

(c) What level of speech accuracy do you need? In other words, how quickly do you need an accurate
recognition? Does a missed recognition hurt the progress of the game?

    I would say that we need a relatively high level of speech accuracy given that it needs to be a
    semi-prominent feature of the game. Given that applications that we talked about in part a,
    any missed recognitions could hinder the user gameplay, causing their performance to suffer.

(d) Do you need specific hardware, specific conditions, etc. to have a reasonable confidence that it
works well enough?

    None that I can think of. I think our computer microphones or airpods work accurately enough for now.