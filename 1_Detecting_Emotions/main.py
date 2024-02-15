input_str = input()
# TODO: Split the input into a list of strings and convert it to a new list of integers
str_list = input_str.split(",")
int_list = [int(str_num) for str_num in str_list]


# TODO: Define a function to analyze the predominant emotion based on the list of
#  integers representing the intensity and a list of strings representing the emotions
def analyze_emotion(facial_features):
    # TODO: Finding the index of the predominant emotion in the list of facial features
    predominant_emotion_index = facial_features.index(max(facial_features))
    emotions = ["Anger", "Happiness", "Sadness", "Surprise"]

    # TODO: Determining the predominant emotion based on the found index
    predominant_emotion = emotions[predominant_emotion_index]
    print(predominant_emotion)


# TODO: Print the predominant emotion
analyze_emotion(int_list)
