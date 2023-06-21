#pip install pywhatkit
import pywhatkit

#contact phone number or group name and your text
contact_number="+919313157673"
#group_name="Python_mini_projects"
text="This message sent from Python!"
#For instantly message
pywhatkit.sendwhatmsg_instantly(contact_number, text)
#For time schedule hours between 0-24
'''hour=12
min=30
pywhatkit.sendwhatmsg(contact_number, text,hour,min)'''
#for group message
#pywhatkit.sendwhatmsg_to_group(group_name,text,hour,min)