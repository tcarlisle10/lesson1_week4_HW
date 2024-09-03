def mood_responses(mood):
    good = ['happy', 'amazing', 'fantastic', 'excited', 'terrific', 'swell', 'joyful', 'grateful', 'peacefully', 'hopefully', 'proud']
    bad = ['angry', 'depressed', 'hopeless', 'overwhelmed', 'anxious', 'mad', 'annoyed']
   
    if mood in good:
        print("That's awesome! I'm glad you are having a good day")
    elif mood in bad:
        print("Oh no! I'm sorry to hear that")