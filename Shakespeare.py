

import re

def process_text(raw_text):
    '''
    1. Remove new lines, periods, colons, apostrophes, parentheses, semicolons frmo the text
    2. Convert string into a list of words
    3. Remove common stop words
    '''
    stopwords = ['','with','i','me','my',
    'to','in','for','the','then','but','a','do','when',
    'where','why','which','who','what',
    'on','that','thy','thus','by','thee',
    'all','have','they','their','his','like',
    'so','into','her','be','or','we','will','and','from',
    'whose','of','if','may','these']
    clean_text = re.sub(pattern='(\\n|\.|:|,|\'s|\(|\)|;)',string=raw_text, repl=' ')
    clean_text = clean_text.lower()
    words      = re.split(pattern='\s{1,}',string=clean_text)
    no_stopwords= set(words) - set(stopwords)
    return list(no_stopwords)

def count_per_word(word_list):
    count_dict = {}
    for word in word_list:
        if word not in count_dict:
            count_dict[word] = 0
        count_dict[word] += 1
    return count_dict



shakespeare_sonnet1 = '''Weary with toil, I haste me to my bed,
The dear repose for limbs with travel tired;
But then begins a journey in my head,
To work my mind, when body's work's expired:
For then my thoughts (from far where I abide)
Intend a zealous pilgrimage to thee,
And keep my drooping eyelids open wide,
Looking on darkness which the blind do see:
Save that my soul's imaginary sight
Presents thy shadow to my sightless view,
Which, like a jewel hung in ghastly night,
Makes black night beauteous and her old face new.
Lo, thus, by day my limbs, by night my mind,
For thee, and for myself, no quiet find.
'''

shakespeare_sonnet2 = '''All the world's a stage,
And all the men and women merely players;
They have their exits and their entrances,
And one man in his time plays many parts,
His acts being seven ages. At first, the infant,
Mewling and puking in the nurse's arms.
Then the whining schoolboy, with his satchel
And shining morning face, creeping like snail
Unwillingly to school. And then the lover,
Sighing like furnace, with a woeful ballad
Made to his mistress' eyebrow. Then a soldier,
Full of strange oaths and bearded like the pard,
Jealous in honor, sudden and quick in quarrel,
Seeking the bubble reputation
Even in the cannon's mouth. And then the justice,
In fair round belly with good capon lined,
With eyes severe and beard of formal cut,
Full of wise saws and modern instances;
And so he plays his part. The sixth age shifts
Into the lean and slippered pantaloon,
With spectacles on nose and pouch on side;
His youthful hose, well saved, a world too wide
For his shrunk shank, and his big manly voice,
Turning again toward childish treble, pipes
And whistles in his sound. Last scene of all,
That ends this strange eventful history,
Is second childishness and mere oblivion,
Sans teeth, sans eyes, sans taste, sans everything.
'''

marlowe_poem = '''Come live with me and be my love,
And we will all the pleasures prove
That valleys, groves, hills, and fields,
Woods, or steepy mountain yields.
And we will sit upon rocks,
Seeing the shepherds feed their flocks,
By shallow rivers to whose falls
Melodious birds sing madrigals.

And I will make thee beds of roses
And a thousand fragrant poises,
A cap of flowers, and a kirtle
Embroidered all with leaves of myrtle;

A gown made of the finest wool
Which from our pretty lambs we pull;
Fair lined slippers for the cold,
With buckles of the purest gold;

A belt of straw and ivy buds,
With coral clasps and amber studs;
And if these pleasures may thee move,
Come live with me, and be my love.

The shepherds's swains shall dance and sing
For thy delight each May morning:
If these delights thy mind may move,
Then live with me and be my love.
'''

ss1 = process_text(shakespeare_sonnet1)
ss2 = process_text(shakespeare_sonnet2)
mrlw= process_text(marlowe_poem)

print('Words that are shared between Shakespeare Sonnet 2 and Marlowee')
print(set(ss2) & set(mrlw))
print("No I dont think Marlowe wrote for shakespeare because even shakespeares own work doesnt include alot of smilarilites just from comparing his two pieces  ")