"""
Bilal Chaudhry
10 March, 2022
Text should not be cut but however if you cannot see it then please try to resize the window
"""

from tkinter import *
 
 
w=Tk()
w.geometry('1300x1300')
w.configure(bg='#262626')
w.resizable(1,1)
w.title('ISU - Student Application Portal')
 
 
 
 
def default_home():
   
    f2 = Frame(w, width=1300, height=1300, bg='#262626')
    f2.place(x=0,y=45)#45
    l2=Label(w,text="ISU \n Student Application Portal",fg='#f4a950',bg='#262626')
    how_to = Label(w,text= "Welcome !!" '\n' 'Click on the "click here" button on the top left of the page to open the menu bar'
    "\n- Bilal C",
    fg='#0f9d9a',bg='#262626')
    how_to.config(font=('Comic Sans MS', 15))
    how_to.place(x=375, y=305)
    l2.config(font=('Comic Sans MS',40))
    l2.place(x=375,y=105)
 
def mac():
   
 
    f1.destroy()
    f2 = Frame(w, width=1300, height=1300, bg='#262626')#455
    f2.place(x=0,y=45)

    head = Label(w,text= " Some applications unique to macOS are -",fg='#f4a950',bg='#262626')
 
    l2=Label(w,text= "\n \nSafari - It's a web browser application that is only available on systems that use macOS and iOS."
    '\n' "In Safari the user can use search engines such as google and yahoo to find information on the world wide web and is its purpose. Some of the features""\nof safari would be book marks, history and "
    '\n' "private browsing mode in which does not keep your search history. \n \nApp store - App store is an application that lets developers publish their apps, so that other users   "
    '\n' "can buy them or download them for free. A feature of the app store would be that users can rate the app out of 5 stars or write a written review. App store is also exclusive "
    '\n'"to apples devices \n \nSiri - Siri is a virtual assistant that is built in every device that uses Apples operating system. The purpose of Siri is to enhance the user experience "
    '\n'"by making tasks like calling/messaging someone or searching something easier and faster. As siri can be used to call or message someone. \n \nPhotos - Is an app that is dedicated"
     "to your pictures. The purpose is to let users manage their photos. Using the app you can make folders to organize your photos.\nUsing the app you can also share your photos with others."
    "There is an editing feature built that lets you edit your photos. For example you can make your photos \nlighter. You can also delete photos using this app.\n \n"
    "Mail - The purpose of the mail app is to allow users to see their electronic mail. Users can access their gmail, outlook and icloud in this one app. It can be used to send emails to \nother users."
    "The user can also flag important messages or simply delete messages using the mail app. The app can be used in 32 languages. \n \nMaps - Maps is an application that is exclusive to all Apple devices."
    "Maps is an app that lets you look at the map of the entire world. The purpose of the app is to give \ndirections to users. It provides the user the distance, estimated time of arrival and the street names. "
    "\n\nImovie - Is a video editing software. The purpose of it is to allow the user to edit video and this could include cutting, trimming, cropping, rotating, speeding up or down,"
    "\nadjusting the color, adding text, graphics and music to the video. \n\nApple Music - You can listen to music in this app if you pay the monthly subscription. You can listen to"
    "radio stations for free. \n\nNotes - Is a note taking app that lets the user take notes quickly together with multiple people, share it with other people, use tables, checklists,draw stuff,"
    "\ndifferent types of fonts and colour, web links. \n\nIcloud - In iCloud you can store files in the cloud. Basically it means that you don’t have to save files on your computer."
    "You can access them on other computers if \nyou're using the same icloud account. The purpose is to let people store their files in the cloud" 
    "\n\nApple News - Its purpose is to show users the latest news. On the top users can read articles, newspapers and magazines on stuff that is happening in the world"
    



    ,fg='#0f9d9a',bg='#262626')
    head.config(justify='left', font=('Comic Sans MS',30, 'bold'))
    head.place(x=50,y=40)
 
    l2.config(justify='left', font=('Comic Sans MS',10, 'bold'))
    l2.place(x=50,y=98)#290
    toggle_win()
 
 
def sources():
    f1.destroy()
 
    f2 = Frame(w, width=1300, height=1300, bg='#262626')
    f2.place(x=0,y=45)
    head = Label(w,text= " Sources -",fg='#f4a950',bg='#262626')
    l2=Label(w,text= '\n''\n' '\n'" ● https://workspace.google.com/intl/en_ca/pricing.html" '\n' '\n'" ● https://support.microsoft.com/en-us/office/use-live-captions-in-a-live-event-1d6778d4-6c65-4189-ab13-e2d77beb9e2a"
    '\n''\n' " ● https://docs.microsoft.com/en-us/microsoftteams/manage-whiteboard" '\n' '\n'" ● https://support.microsoft.com/en-us/office/get-started-with-microsoft-teams-b98d533f-118e-4bae-bf44-3df2470c2b12#:~:text=Microsoft%20Teams%20is%20a%20"'\n''\n'"   collaboration,projects%2C%20or%20just%20for%20fun."
    '\n' '\n' " ● https://support.skype.com/en/faq/fa6/what-is-skype#:~:text=Skype%20is%20software%20that%20enables,with%20other%20people%20on%20Skype." '\n' '\n' " ● https://www.compete366.com/blog-posts/microsoft-teams-what-is-it-and-should-we-be-using-it\n   /#:~:text=Microsoft%20Teams%20is%20a%20persistent,and%20communicate%20with%20one%20another." '\n''\n'
    " ● https://www.apple.com/ca/maps/" '\n' '\n' " ● https://www.apple.com/ca/ios/photos/" '\n' '\n' " ● https://www.apple.com/ca/siri/" '\n' '\n' " ● https://www.makeuseof.com/tag/complete-guide-default-mac-apps/" '\n' '\n' " ● https://www.howtogeek.com/224746/screenshot-tour-the-29-new-universal-apps-included-with-windows-10/" '\n' '\n' " ● https://www.d2l.com/k-12/brightspace-comparison/" '\n''\n'
    " ● https://comparecamp.com/google-classroom-vs-brightspace-comparison/" '\n' '\n' " ● https://www.techlearning.com/features/what-is-google-classroom" '\n' '\n' " ● https://iopscience.iop.org/article/10.1088/1742-6596/1175/1/012165/pdf#:~:text=Google%20Classroom%20is%20a%20part,sending%20feedback%20and%20providing%20homework."
 
 
   
 
    ,fg='#0f9d9a',bg='#262626')

    head.config(justify='left', font=('Comic Sans MS',30, 'bold'))
    head.place(x=50,y=50)

    l2.config(justify='left', font=('Comic Sans MS',10, 'bold'))
    l2.place(x=50,y=105)
    toggle_win()
 
def teams():
    f1.destroy()
 
    f2 = Frame(w, width=1300, height=1300, bg='#262626')
    f2.place(x=0,y=45)
    head = Label(w,text= "Microsoft Teams VS Google meet",fg='#f4a950',bg='#262626')
    l2=Label(w,text= "Microsoft Teams and Google meets are two apps that have the same purpose. Their purpose is to let people collaborate with each other. People are able to collaborate "
    '\n' "with each other on both softwares by starting a meet, which is essentially a voice call in which users can chat and share their screens with each other. " '\n' '\n' "On my student "
    "portal I would add Microsoft teams rather than Google meets because - " '\n''\n' "  ● The amount of people that are able to join a meeting is really important because some organizations/classes "
    "are very big, so it is important for them that a lot of people" '\n' "    are able to join a meeting. 250 people can join a teams meet, while only 100 people can join a google meet." '\n''\n' "  ● "
    "Video quality is also another important factor. The maximum video for Google Meet is 720p while Microsoft Team's maximum video quality is 1080p. This means that the" '\n' "    video quality is better on Microsoft Teams. "'\n''\n'
    "  ● Recording meets is also an important feature, as sometimes people may have to refer to older meetings, unfortunately recording meetings is not free on both platforms." '\n' "    But to record a meet on "
    "google meets you need to buy the “business standard” plan which costs around $15.60 per month. However you can record microsoft teams meeting" '\n' "    with their E1 plan which is $12.80 per month. "
    '\n''\n' "  ● A lot of people from all around the world use Microsoft teams. So they have a feature in which users can send messages to each other on Microsoft teams and they can "
    '\n' "    also translate messages in other languages such as Arabic, Bosnian, Bulgarian, Catalan, Creole, Czech, Danish, Dutch, English, Estonian, Filipino . You cannot however"
    '\n' "    you can not translate messages on Google meet. " '\n''\n' "  ● Some people like using apps rather than using their browser versions. In Microsoft teams you have the ability to download their app or use their website using a search engine."
    '\n' "    But Google meet does not have a desktop application, so the only option is to use their website.  "
    '\n' '\n'"  ● Google meet subtitles are only available in English, Portuguese, French, German and Spanish. While in teams , some available languages are English, Chinese, Dutch, French,"
    '\n' "    German, Hindi, Italian, Japanese, Korean, Portuguese, Russian and more. " '\n''\n' "  ● You can take notes inside of OneNote using just Microsoft teams, its a built in feature of Microsoft-Teams. This is helpful as users can open one note directly from Microsoft-"
    '\n' "    teams and take notes. Sadly Google meet has no such feature." '\n' "  ● In microsoft teams you can send other users files from your computer. But Google meets does not have a feature like this. "
    '\n' '\n'"  ● Is a digital canvas on which the user can write and draw and share it with other people. However google meet doesn't have a feature like this. "
    '\n''\n'"  ● There are many different default themes available on Microsoft teams that could be used to change the background colour of the microsoft teams UI. For example"
    '\n' "    there's a dark mode and Google meets has no such option. Users are forced to use their default colours. "
 
 
    ,fg='#0f9d9a',bg='#262626')
    head.config(justify='left', font=('Comic Sans MS',30, 'bold'))
    head.place(x=50,y=50)
    l2.config(justify='left', font=('Comic Sans MS',10, 'bold'))
    l2.place(x=50,y=120)
    toggle_win()
 
def windows():
    f1.destroy()
 
    f2 = Frame(w, width=1300, height=1300, bg='#262626')
    f2.place(x=0,y=45)
    head = Label(w,text= " Some applications unique to windows are -",fg='#f4a950',bg='#262626')
    l2=Label(w,text= '\n' '\n' " ● Edge - It's also a web browser that lets you search things on the browser. It is made by Microsoft, so "
    "so it's the default browser for Windows 10.\n   The purpose is the same as chrome or Safari, to access information on the world wide web.\n\n ● Microsoft Store - This app is like the "
    "App store. Developers are able to publish their apps on the store and people can then download the apps on their\n   devices. Like Google has published the chrome application in the"
    "microsoft store and now through the microsoft store I can download Chrome." '\n''\n' " ● Photos - Lets you look at the photos and videos on your computer. Users can delete and send files"
    "using the app. Another thing people can do is edit \n   their pictures. For instance users can add text on your photo or video.\n\n ● Mail - The mail application allows the user to look" 
    "at their electronic mail. Users can also send emails to other users using the mail app. They can do \n   much more than just receive and send emails. They can organize their emails by making folders." 
    "\n\n ● Paint - Is a basic graphics/painting app. The purpose of paint is to let the user draw, colour and edit pictures. For instance you can draw a picture"
    "\n   in it using the marks and pens and you import an image in the program and then resize. There is much more that can happen in that program but these are the basics. "
    "\n\n ● Snipping tool - Purpose of snipping tool is to let users take screenshots of their screen. They can also crop the image when taking a screenshot."
    "\n   Although the main purpose of the snipping tool is to take screenshots, users can also draw on images using their pen feature. "
    "\n\n ● File explorer - The main purpose of the file explorer is to let users access your files. But there is more that you can do with the file explorer." 
    "\n   You can organize your files. Like you can make a folder for your school files to make it more organized. Users can also copy paths of files." 
    "\n\n ● Calculator - MacOs also has a pre-installed application called Calculator. They both have the same purpose but they are different. Their purpose" 
    "\n   is to let the users perform math operations. Like in the calculator I can divide, multiply, subtract, add and get the square root of the number."
    "\n\n ● Skype - The purpose of skype is to allow people to communicate with each other. Using skype users can video call and message each other for free."
    "\n\n ● Weather - Tells its users what weather they should expect in the next few hours and this is its purpose. " "\n\n ● Solitaire collection - Purpose of this app is very simple, it lets the user play the game solitaire on their computer. "

  
   
 
    ,fg='#0f9d9a',bg='#262626')

    head.config(justify='left', font=('Comic Sans MS',30, 'bold'))
    head.place(x=50,y=50)

    l2.config(justify='left', font=('Comic Sans MS',10, 'bold'))
    l2.place(x=50,y=105)

    toggle_win()
 

def both():
   
 
    f1.destroy()
    f2 = Frame(w, width=1300, height=1300, bg='#262626')#455
    f2.place(x=0,y=45)
    head = Label(w,text= " Apps typically installed on both operating systems -",fg='#f4a950',bg='#262626')
 
    l2=Label(w,text= " \n \n   ● Chrome - Is a web browser like safari and Microsoft Edge. The purpose is the same like any other web browser. Its main purpose"
    "\n     is to allow users to search for information on the world wide web. It has the same features as the other web browsers, for example chrome""\n     also has tabs and bookmarks. The only difference is that"
    "chrome is the fastest web browser and it is available on almost all operating systems." '\n \n' "   ● Microsoft teams - is a communication app that lets you in touch with your team. It is built for hybrid work, so the main purpose is to make" 
    "\n     communication easier with other people. In microsoft teams users can host meetings so that others can join. You can also create a team and make""\n     announcements and assign work in the team. "
    "\n \n   ● Office - The purpose of the office application is to allow the user to access all the Microsoft softwares such as Word, Excel and powerpoint in"
    "\n     one place. For example, through Microsoft Office you can open Microsoft Word."
    "\n \n   ● Onedrive - The purpose is to store files on the cloud and make sharing files easier. It stores the files on a server. It does not store stuff "
    "\n     inside your computer's harddrive or ssd. You can open the files stored on onedrive using another computer if you have access to that onedrive account."
    "\n     Users can also send other onedrive users the files through onedrive.  "
    "\n \n   ● Adobe premiere pro - Purpose of Adobe premiere pro is to let the users edit their videos. For example using premiere pro users can cut/add footage."
    "\n     Another thing they can do is add audio to their video. You can do much more in premiere pro but the main purpose is make video editing easy. "
    "\n \n   ● VScode - Vscode is a code editor, its purpose is to let users write code and then run the code."

    



    ,fg='#0f9d9a',bg='#262626')
   
    head.config(justify='left', font=('Comic Sans MS',30, 'bold'))
    head.place(x=50,y=50)
    l2.config(justify='left', font=('Comic Sans MS',12, 'bold'))
    l2.place(x=50,y=105)#290
    toggle_win()

def brightspace():
    f1.destroy()
 
    f2 = Frame(w, width=1300, height=1300, bg='#262626')
    f2.place(x=0,y=45)

    head = Label(w,text= "Brightspace VS Google Classroom",fg='#f4a950',bg='#262626')

    l2=Label(w,text= "The purpose of google classroom and brightspace is to make communication easier with people. This includes giving feedback, talking to others, useful widgets," 
    "\nsharing files, joining a video call and assigning tasks to people. They are intended for students but they are also very good for a workplace team." 
    " In my opinion Brightspace is \nmuch better than Google classroom. Brightspace is better and I would keep it in my portal because - "
    "\n \n   ● Brightspace has a quiz feature built in it. Which means that students can complete the quiz inside the brightspace app. They don’t need to go to a third party website."
    "\n     The quiz feature is very good, as it is much harder to cheat on and there is a timer on the top. While in google classroom there is no such feature like this."
    "\n     Teachers need to use a third party website and then post the link in the stream. "
    "\n \n   ● There is a discussion feature on brightspace which is very helpful. Students can have discussions with people inside the class on the website.  The discussions can be"
    "\n     very helpful as communicating with other students is very easy and fast. They can also be public for some students and private for some. There are a lot of things that"
    "\n     you can do in it. The discussion also keeps the activity feed organized as the discussions are not happening in the feed. But google classrooms have no such feature like this."
    "\n     Teachers and students can talk by making a post but there is no proper place to have discussions."
    "\n \n   ● As students complete their assignments and tests, brightspace automatically calculates your final percentage for you but google classroom does not do that.This is handy as"
    "\n     teachers don’t have to manually calculate the percentage of each individual student."
    "\n \n   ● On brightspace, at the top right of the screen there is an inbox which is very nice as you get notifications over there and it's just a good reminder. Sadly there is no" 
    "\n     inbox available on google classroom."
    "\n \n   ● D2L has more widgets and the widgets are very convenient. Both of the websites, google classroom and D2l have a work to do widget but D2l has more than just that."
    "\n     D2l has a calendar, Britannia science launch pack, TVO quick links and a Google workspace widget. These widgets make life much easier. For instance, because of the"
    "\n     google workspace widget I don’t need to go to the Gmail website to check my emails, I can check them straight from D2l. "
    "\n \n   ● In google classrooms the maximum number of students allowed in one classroom is 1000. However on D2l the maximum number of students allowed in one classroom is 3000. "
 
 
    ,fg='#0f9d9a',bg='#262626')

    head.config(justify='left', font=('Comic Sans MS',30, 'bold'))
    head.place(x=50,y=50)

    l2.config(justify='left', font=('Comic Sans MS',10, 'bold'))
    l2.place(x=50,y=178)

    toggle_win()
 
def toggle_win():
   
    global f1
 
    f1 = Frame(w,width=300,height=1500,bg='#f4a950')# side bar
    f1.place(x=0,y=0)
   
   
 
    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
 
   
 
 
        def on_entera(e):
           
 
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33
           
 
        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'
 
        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                     
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)
 
        myButton1.place(x=x,y=y)
 
    bttn(0,80,'Applications exclusive to macOS','#0f9d9a','#f4a950',mac)
    bttn(0,117,'Applications exclusive to Windows','#0f9d9a','#f4a950',windows)
    bttn(0,154,'Applications avaliable on both operating systems','#0f9d9a','#f4a950',both)
    bttn(0,191,'Apps that have the same purpose #1','#0f9d9a','#f4a950',teams)
    bttn(0,228,'Apps that have the same purpose #2','#0f9d9a','#f4a950',brightspace)
    bttn(0,265,'Sources','#0f9d9a','#f4a950',sources)
 
    
    def dele():
        f1.destroy()
 
   
    Button(f1,
           text="Click here to close",
           border=0,
           command=dele,
           bg='#f4a950',
           activebackground='#f4a950').place(x=5,y=10)#12c4c0
   
 
 
 
Button(w,text="Click here",
       command=toggle_win,
       border=0,
       fg='#f4a950',
       bg='#262626',
       activebackground='#f4a950').place(x=5,y=10)
 
default_home()
 
w.mainloop()

