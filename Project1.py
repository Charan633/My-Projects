#Fun qiuz with 10 questions. 4 options each.
score=0

#Introduction
print("FUN QUIIZ \n")
print("\n Hi my name is SAM (Super Automated Machine).")

#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

name1=input("What is your name? ")
print("\n Nice meeting you",name1,".","Welcome to the FUN QUIZ. \n The rules of the game are simple. You'll get to choose the topic on which you want to take the quiz. \n You'll have 10 questions(each having 4 options out of which 1 is correct)")
choice=int(input("\n I want you to choose a topic for the quiz: \n 1.SPORTS(1) \n 2.MOVIES(2) \n 3.AEROSPACE(3) \n 4.GENERAL KNOWLEDGE(4) \n 5.DPS-MIS(5) \n Your choice:"))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#choice is 1
if (choice==1):
    print("\n Well you seem to be interested in sports,",name1,"\n All the best.")

    q1=input("\n Q1.Which sport has the most number of viewers? \n (a)Cricket \n (b)Football \n (c)Tennis \n (d)Hockey \n Answer: ")
    if(q1=="b"):
        score=score+1
        print("Congrats. You are right. Football has 3.5 billion viewers making it the most viewed sport in the world.")
    else:
        print("Sorry, the correct answer is (b)Football. Football has 3.5 billion viewers making it the most viewed sport in the world.")

    q2=input("\n Q2.How many players are there in a basketball team?(excluding the substitutes) \n (a)5 \n (b)6 \n (c)7 \n (d)8 \n Answer: ")
    if(q2=="a"):
        score=score+1
        print("Congrats. You are right. There are 5 players in a basketball team.")
    else:
        print("Sorry, the correct answer is (a)5")

    q3=input("\n Q3.How many feathers are there in a badminton shuttlecock? \n (a)14 \n (b)16 \n (c)18 \n (d)15 \n Answer: ")
    if(q3=="b"):
        score=score+1
        print("Congrats. You are right. There are 16 feathers in a standard badminton shuttlecock.")
    else:
        print("Sorry, the correct answer is (b)16")

    q4=input("\n Q4.Which country has won the most FIFA world cups? \n (a)Argentina \n (b)Germany \n (c)Italy \n (d)Brazil \n Answer: ")
    if(q4=="d"):
        score=score+1
        print("Congrats. You are right. Brazil has won the FIFA world cup 5 times, followed by Germany(4 times), Italy(4 times) and Argentina(2 times).")
    else:
        print("Sorry, the correct answer is (d)Brazil. Brazil has won the FIFA world cup 5 times, followed by Germany(4 times), Italy(4 times) and Argentina(2 times).")

    q5=input("\n Q5.National sport of China is: \n (a)Badminton \n (b)Taekwondo \n (c)Table Tennis \n (d)None of these \n Answer: ")
    if(q5=="c"):
        score=score+1
        print("Congrats. You are right. Table Tennis is China's national sport. China won 6 gold medals in table tennis during the London Olympics in 2012.")
    else:
        print("Sorry, the correct answer is (c)Table Tennis. Table Tennis is China's national sport. China won 6 gold medals in table tennis during the London Olympics in 2012.")

    q6=input("\n Q6.Who invented Chess? \n (a)Persians \n (b)Chinese \n (c)Greeks \n (d)Indians \n Answer: ")
    if(q6=="d"):
        score=score+1
        print("Congrats. You are right.The most commonly held belief is that chess originated in India, where it was called Chaturanga, which appears to have been invented in the 6th century AD.")
    else:
        print("Sorry, the correct answer is (d)Indians.The most commonly held belief is that chess originated in India, where it was called Chaturanga, which appears to have been invented in the 6th century AD.")

    q7=input("\n Q7.What is the world record time for 200 meters in running(in seconds)? \n (a)18.10 \n (b)19.13 \n (c)18.19 \n (d)19.19 \n Answer: ")
    if(q7=="d"):
        score=score+1
        print("Congrats. You are right. The world record holder for 200m is Usain Bolt of Jamaica, who ran 19.19s at the 2009 World Championships.")
    else:
        print("Sorry, the correct answer is (d)19.19sec. The world record holder for 200m is Usain Bolt of Jamaica, who ran 19.19s at the 2009 World Championships.")

    q8=input("\n Q8.Who is the father of Indian hockey? \n (a)Roop Singh \n (b)Manpreet Singh \n (c)Dhyan Chand \n (d)Suraj Karkera \n Answer: ")
    if(q8=="c"):
        score=score+1
        print("Congrats. You are right. Dhyan Chand is considered the father of Indian hockey.")
    else:
        print("Sorry, the correct answer is (c)Dhyan Chand.Dhyan Chand is considered to be the father of Indian hockey.")

    q9=input("\n Q9.Who has won the most Golden Boot award? \n (a)Thierry Henry \n (b)Lionel Messi \n (c)Cristiano Ronaldo \n (d)Paul Pogba \n Answer: ")
    if(q9=="a"):
        score=score+1
        print("Congrats. You are right.Thierry Henry has won the most Golden Boot awards (4 times).")
    else:
        print("Sorry, the correct answer is (a)Thierry Henry.Thierry Henry has won the most Golden Boot awards (4 times).")

    q10=input("\n Q10.How matches did Mohammed Ali lose in his career? \n (a)56 \n (b)5 \n (c)1 \n (d)37 \n Answer: ")
    if(q10=="b"):
        score=score+1
        print("Congrats. You are right.In his professional career, Mohammed Ali won 56 bouts and lost only five.")
    else:
        print("Sorry, the correct answer is (b)5.In his professional career, Mohammed Ali won 56 bouts and lost only five.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#choice is 2
elif (choice==2):
    print("\n All the best",name1,"\n LIGHTS CAMERA ACTION",)

    q1=input("\n Q1.Which film has won the most Oscars of all time? \n (a)Titanic (1997) \n (b)Ben-Hur (1959) \n (c)The Lord of the Rings: The Return of the King (2003) \n (d)All of these \n Answer: ")
    if(q1=="d"):
        score=score+1
        print("Congrats. You are right. Three films hold the record of winning the most Academy Awards, having garnered 11 Oscars each: Ben-Hur (1959), Titanic (1997) and The Lord of the Rings: The Return of the King (2003).")
    else:
        print("Sorry, the correct answer is (d)All of these. Three films hold the record of winning the most Academy Awards, having garnered 11 Oscars each: Ben-Hur (1959), Titanic (1997) and The Lord of the Rings: The Return of the King (2003).")

    q2=input("\n Q2.What is the name of the kingdom where the 2013 animated movie Frozen is set? \n (a)Arendelle \n (b)Auradon \n (c)Moors \n (d)Corona \n Answer: ")
    if(q2=="a"):
        score=score+1
        print("Congrats. You are right. The kingdom is Arendelle .")
    else:
        print("Sorry, the correct answer is (a)Arendelle")

    q3=input("\n Q3.In which 1984 science fiction movie did Linda Hamilton play the role of Sarah Connor? \n (a)King Kong Lives \n (b)The Terminator \n (c)Last Action Hero \n (d)None of these \n Answer: ")
    if(q3=="b"):
        score=score+1
        print("Congrats. You are right. Linda Hamilton played the role of Sarah Connor in The Terminator sequels.")
    else:
        print("Sorry, the correct answer is (b)The Terminator")

    q4=input("\n Q4.Who played Jack Dawson in the 1997 epic Titanic? \n (a)Jack Nicohlson \n (b)Jason Barry \n (c)Leonardo DiCaprio \n (d)Matt Damon \n Answer: ")
    if(q4=="c"):
        score=score+1
        print("Congrats. You are right. Leonardo DiCaprio played the role of Jack Dawson in the 1997 epic Titanic.")
    else:
        print("Sorry, the correct answer is (c)Leonardo DiCaprio")

    q5=input("\n Q5.The genie ,in the film Aladdin(1992), was voiced by: \n (a)Robbie Williams \n (b)Eddie Murphy \n (c)Robin Williams \n (d)Jonathan Winters \n Answer: ")
    if(q5=="c"):
        score=score+1
        print("Congrats. You are right. The genie was voiced by Robin Williams.")
    else:
        print("Sorry, the correct answer is (c)Robin Williams")

    q6=input("\n Q6.Name the Indian film(s) that was/were nominated for the Oscars? \n (a)Mother India(1957) \n (b)Salaam Bombay(1988) \n (c)Lagaan(2001) \n (d)All of these \n Answer: ")
    if(q6=="d"):
        score=score+1
        print("Congrats. You are right.As of 2019, only three Indian films—Mother India (1957), Salaam Bombay! (1988) and Lagaan (2001)—have been nominated for the award.")
    else:
        print("Sorry, the correct answer is (d)All of these")

    q7=input("\n Q7.Either you're the one erasing or you're the one being erased- who said this? \n (a)Jim Carrey \n (b)Bruce Lee \n (c)Tom Hanks \n (d)Morgan Freeman \n Answer: ")
    if(q7=="a"):
        score=score+1
        print("Congrats. You are right. Jim Carrey quoted this.")
    else:
        print("Sorry, the correct answer is (a)Jim Carrey")

    q8=input("\n Q8.For which film did Jackie Chan win Oscar? \n (a)Rush Hour \n (b)Chinese Zodiac \n (c)The Foreigner \n (d)None Of These \n Answer: ")
    if(q8=="d"):
        score=score+1
        print("Congrats. You are right. Jackie Chan didn't win the Oscar for any particular film. He received the award as a life time achievement award.")
    else:
        print("Sorry, the correct answer is (d)None of these.Jackie Chan didn't win the Oscar for any particular film. He received the award as a life time achievement award.")

    q9=input("\n Q9.In the movie 'How the Grinch Stole Christmas', who plays as the 'Grinch'? \n (a)Jim Carrey \n (b)Tom Hanks \n (c)Adam Sandler \n (d)Robin Williams \n Answer: ")
    if(q9=="a"):
        score=score+1
        print("Congrats. You are right.Jim Carrey plays the role of the Grinch in the movie..")
    else:
        print("Sorry, the correct answer is (a)Jim Carrey")

    q10=input("\n Q10.What was the name of the mineral that the RDA mined in the movie 'Avatar' ? \n (a)Saronite \n (b)Unobtanium \n (c)Necrodermis \n (d)Adamantium \n Answer: ")
    if(q10=="b"):
        score=score+1
        print("Congrats. You are right.The Resources Development Administration (RDA for short) mines for a valuable mineral — unobtanium — on Pandora, a densely forested habitable moon orbiting the gas giant Polyphemus in the Alpha Centauri star system.")
    else:
        print("Sorry, the correct answer is (b)Unobtanium. The Resources Development Administration (RDA for short) mines for a valuable mineral — unobtanium — on Pandora, a densely forested habitable moon orbiting the gas giant Polyphemus in the Alpha Centauri star system.")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#choice is 3
elif (choice==3):
    print("\n All the best",name1,"\n YOU ARE CLEARED FOR TAKE-OFF")

    q1=input("\n Q1.Which aircraft is nick named as 'Jumbo Jet'? \n (a)A380-800 \n (b)Airbus Beluga \n (c)Antonov \n (d)Boeing 747-400 \n Answer: ")
    if(q1=="d"):
        score=score+1
        print("Congrats. You are right. The Boeing 747-400 is also called as the Jumbo Jet.")
    else:
        print("Sorry, the correct answer is (d)Boeing 747-400")

    q2=input("\n Q2.What was the maximum speed of Concorde? \n (a)2179km/h \n (b)2430km/h \n (c)3529km/h \n (d)2681km/h \n Answer: ")
    if(q2=="a"):
        score=score+1
        print("Congrats. You are right. The max speed ever recorded for this aircraft was 2179km/h .")
    else:
        print("Sorry, the correct answer is (a)2179km/h")

    q3=input("\n Q3.What is the distance between Earth and Moon? \n (a)364,500 km \n (b)384,400 km \n (c)465,000 km \n (d)None of these \n Answer: ")
    if(q3=="b"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (b)384,400 km")

    q4=input("\n Q4.How many missions have landed on the moon? \n (a)9 \n (b)11 \n (c)6 \n (d)None Of These \n Answer: ")
    if(q4=="c"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (c)6. The last mission was on 11th December 1972.")

    q5=input("\n Q5.What was the cost of Mangalyaan mission? \n (a)USD 50 million \n (b)USD 165 million \n (c)USD 73 million \n (d)USD 250 million \n Answer: ")
    if(q5=="c"):
        score=score+1
        print("Congrats. You are right. The total cost of the mission was around ₹ 450 Crore or USD 73 million. The low cost was because of the simple design, reduced work cost and use of home technology.")
    else:
        print("Sorry, the correct answer is (c)USD 73 million")

    q6=input("\n Q6.Which planet is closest to the Earth? \n (a)Venus \n (b)Mars \n (c)Moon \n (d)Mercury \n Answer: ")
    if(q6=="d"):
        score=score+1
        print("Congrats. You are right.The answer most people would give is Venus. But … it might actually be Mercury. Although Venus is the planet that comes closest to Earth as it sweeps by on its orbit, Mercury stays the closest to Earth the longest.")
    else:
        print("Sorry, the correct answer is (d)Mercury")

    q7=input("\n Q7.What is the distance of the ISS from Earth's surface? \n (a)408km \n (b)700km \n (c)588km \n (d)608km \n Answer: ")
    if(q7=="a"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (a)408km")

    q8=input("\n Q8.Which is the first country to reach Mars on its first attempt? \n (a)USA \n (b)China \n (c)USSR \n (d)India \n Answer: ")
    if(q8=="d"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (d)India")

    q9=input("\n Q9.Name the first artificial satellite sent to space. \n (a)Sputnik \n (b)Apollo \n (c)GeoSat-1 \n (d)None of these \n Answer: ")
    if(q9=="a"):
        score=score+1
        print("Congrats. You are right.Sputnik was the first artificial sent to space by USSR.")
    else:
        print("Sorry, the correct answer is (a)Sputnik")

    q10=input("\n Q10.When was the first plane invented? \n (a)1905 \n (b)1903 \n (c)1900 \n (d)1928 \n Answer: ")
    if(q10=="b"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (b)1903")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#choice is 4
elif (choice==4):
    print("\n All the best",name1,"\n")

    q1=input("\n Q1.Which South American country was named after the Italian city of Venice? \n (a)Argentina \n (b)Brazil \n (c)Chile \n (d)Venezuela \n Answer: ")
    if(q1=="d"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (d)Venezuela")

    q2=input("\n Q2.In terms of land area , which was the largest empire of all time? \n (a)British empire \n (b)Ottoman empire \n (c)Roman empire \n (d)Mughal empire \n Answer: ")
    if(q2=="a"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (a)British empire")

    q3=input("\n Q3.Who wrote War and Peace? \n (a)Rabindranath Tagore \n (b)Leo Tolstoy \n (c)Chetan Bhagat \n (d)None of these \n Answer: ")
    if(q3=="b"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (b)Leo Tolstoy")

    q4=input("\n Q4.By number of films, which country has the largest film industry? \n (a)China \n (b)USA \n (c)India \n (d)UK \n Answer: ")
    if(q4=="c"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (c)India")

    q5=input("\n Q5.In which and in which country was the FIFA world cup held? \n (a)1930,USA \n (b)1934,Italy \n (c)1930,Uruguay \n (d)1932,Argentina \n Answer: ")
    if(q5=="c"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (c)1930,Uruguay")

    q6=input("\n Q6.A country historically known as Abyssinia, what is the modern name for it? \n (a)Sudan \n (b)Egypt \n (c)Tunisia \n (d)Ethiopia \n Answer: ")
    if(q6=="d"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (d)Ethiopia")

    q7=input("\n Q7.Which country has the largest coastline? \n (a)Canada \n (b)India \n (c)USA \n (d)Greenland \n Answer: ")
    if(q7=="a"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (a)Canada")

    q8=input("\n Q8.In which sport are the Thomas Cup, Uber Cup and Sudaiman Cup tournaments played? \n (a)Golf \n (b)Lawn Tennis \n (c)Table Tennis \n (d)Badminton \n Answer: ")
    if(q8=="d"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (d)Badminton")

    q9=input("\n Q9.Which fruit contains the most calories? \n (a)Avocado \n (b)Apple \n (c)Orange \n (d)Grape \n Answer: ")
    if(q9=="a"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (a)Avocado")

    q10=input("\n Q10.What is the capital of Mauritius? \n (a)Chamarel \n (b)Port Louis \n (c)Grand Baie \n (d)Mahebourg \n Answer: ")
    if(q10=="b"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (b)Port Louis")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#choice is 5
elif (choice==5):
    print("\n All the best",name1,"\n")

    q1=input("\n Q1.Who is the Patron of DPS-MIS? \n (a)Mr.V.K.Shunglu \n (b)Mr.Yasir Nainar \n (c)Mr.Mohammed Bin Hammam \n (d)Mrs.Aisha Mohammed \n Answer: ")
    if(q1=="d"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (d)Mrs.Aisha Mohammed")

    q2=input("\n Q2.Which school won the Encuesta quiz 2019? \n (a)Rajagiri Public School \n (b)MES \n (c)DPS-MIS \n (d)BPS \n Answer: ")
    if(q2=="a"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (a)Rajagiri Public School")

    q3=input("\n Q3.Who was the Head Boy and Head Girl of the year 2017-18? \n (a)Ganesh and Nayana \n (b)Safwan and Nimra \n (c)Rohit and Samiksha \n (d)Amarnath and Saumya \n Answer: ")
    if(q3=="b"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (b)Safwan and Nimra")

    q4=input("\n Q4.Choose the Games Captains of the year 2019-20? \n (a)Nimisha and Anika \n (b)Andrea and Aadil \n (c)Umang and Sana \n (d)Umang and Nimisha \n Answer: ")
    if(q4=="c"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (c)Umang and Sana")

    q5=input("\n Q5.How many editions of TEDX Youth has been organized by our school? \n (a)6 \n (b)3 \n (c)5 \n (d)4 \n Answer: ")
    if(q5=="c"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (c)5")

    q6=input("\n Q6.Who were the rendezvous winners of the year 2018-19? \n (a)Lotus \n (b)Tulip \n (c)Lily \n (d)Rose \n Answer: ")
    if(q6=="d"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (d)Rose")

    q7=input("\n Q7.How many clubs are there in our school? \n (a)9 \n (b)11 \n (c)10 \n (d)7 \n Answer: ")
    if(q7=="a"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (a)9")

    q8=input("\n Q8.Who is the head of FIITJEE? \n (a)Mr.Aravinda \n (b)Mr.Phani \n (c)Mr.Vivek \n (d)Mr.Sunil \n Answer: ")
    if(q8=="d"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (d)Mr.Sunil")

    q9=input("\n Q9.Which club organized the Book Fair that was held on 21st November 2019? \n (a)Environmental club \n (b)Publication club \n (c)MUN club \n (d)Science club \n Answer: ")
    if(q9=="a"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (a)Environmental club")

    q10=input("\n Q10.Name the captains of the House that won the cultural rendezvous this year. \n (a)Jayanto and Malika \n (b)Abhay and Nanditha \n (c)Johann and Arham \n (d)Namitha and Abhinav \n Answer: ")
    if(q10=="b"):
        score=score+1
        print("Congrats. You are right.")
    else:
        print("Sorry, the correct answer is (b)Abhay and Nanditha")

else:
    print("Invalid input.")
print("\n Your total score is",score,"out of 10")
