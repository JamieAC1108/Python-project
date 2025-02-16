#%%
# this is the actual bot
import string, re

syllable_data = {}

with open('syllables.txt', 'r', encoding='utf-8') as syllable_file:
    for line in syllable_file:
        line = line.strip().lower().replace(',', '').replace('"','').replace('\n', ' ')
        if line:  
            parts = re.split(r'\s*:\s*', line)
            if len(parts) == 2:  
                word = parts[0].strip().lower().replace(',', '').replace('"','').replace('\n', ' ').strip().lower()
                syllable_count = int(parts[1].replace(',', '').replace('"','').replace('\n', ' ').strip().lower())
                syllable_data[word] = syllable_count
            try: 
                syllable_count = int(parts[0].replace(',', '').strip())  
                syllable_data[word] = syllable_count    
            except ValueError:
                    print(f"")
            else:
                print(f"")
                
                

comment_syllable_counts = {}

with open('youtube_comments.txt', 'r', encoding='utf-8') as comment_file:
    youtube_comments = comment_file.readlines()



## Process each comment in the youtube comments
for idx, line in enumerate(youtube_comments):
    columns = line.strip().split('\t')  
    if len(columns) >= 5:  
        comment = columns[4]  
        words = comment.strip().split()  
        total_syllables = 0
        syllable_breakdown = []

        for word in words:
            word_cleaned = word.translate(str.maketrans('', '', string.punctuation)).lower()
            syllable_count = syllable_data.get(word_cleaned, 0)
            total_syllables += syllable_count
            syllable_breakdown.append(syllable_count)

        if sum(syllable_breakdown[: 5]) == 5 and sum(syllable_breakdown[5: 12]) == 7 and sum(syllable_breakdown[12: ]) == 5:
            with open('Haiku.txt', 'w', encoding='utf-8') as haiku_file:
                haiku_file.write(comment)


        # Store the syllable count for this comment
        comment_syllable_counts[idx + 1] = total_syllables 
# %%