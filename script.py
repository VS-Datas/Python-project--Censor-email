# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# email_one, censor a specific word or phrase:

def censor(word, email):
    email = email.replace(word, "---")
    return email

#print(censor('learning algorithms', email_one))

#email_two, censor a whole list of words and phrases:

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def first_clean_list(list_of_words_phrases):
  prep_list = []
  for i in list_of_words_phrases:
    prep_list.append(i + " ")
    prep_list.append(" " + i)
    prep_list.append(i[0].upper() + i[1])
  return prep_list

def censor_list(list_of_words_phrases, email):
  for word in list_of_words_phrases:
     email = email.replace(word, ' *** ')
  return email

print(censor_list(proprietary_terms, email_two))  

# censor negative words use email_three:

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def cleaning_list(negative_words):
  cleaned_list = []
  for i in negative_words:
    cleaned_list.append(i + " ")
    cleaned_list.append(" " + i)
    cleaned_list.append(i[0].upper() + i[1])
  return cleaned_list  


def negative_words_count_2x(
list_of_words_phrases, email):
  list_of_words_phrases_count = 0
  for word in list_of_words_phrases:
    if word in email: 
       list_of_words_phrases_count += 1
    if list_of_words_phrases_count >= 2:
      for word in list_of_words_phrases:
       email = email.replace(word, " **** ")
  return email 

print(negative_words_count_2x(negative_words, email_three)) 


