
import Image, ImageSequence

img = Image.open("white.gif")




for i in img.getdata():
     if i != 0:
          print i



for i in xrange(img.size[0]):
     for j in xrange(img.size[1]):
          if img.getpixel((i,j)) == 8:
               print i,j
     


def get_iterator():
    return ImageSequence.Iterator(Image.open("white.gif"))


N = len(list(get_iterator()))   # it's 133

locations = []
for frame in get_iterator():
    c = list(frame.getdata())
    assert len(c) == 40000
    i = c.index(8)
    y, x = divmod(i, 200)
    locations.append((x, y))

"""

import turtle, time
#turtle puts (0, 0) smack in the middle of the canvas

EXP = 2    # make bigger to draw larger letters
x = y = 0  # center of turtle canvas
for pilx, pily in locations:
    dx = (pilx - 100) // 2  # -1, 0, +1
    dy = (100 - pily) // 2  # -1, 0, +1
    x += dx * EXP
    y += dy * EXP
    turtle.goto(x, y)
    if dx == dy == 0: # joystick at center
        time.sleep(1) # so we can read the letter
        turtle.reset()
        x = y = 0

"""

import ImageDraw
im = Image.open("white.gif")
new = Image.new("RGB", (200, 200))
draw = ImageDraw.Draw(new)

cx,cy = 0,100
for frame in range(133):
    im.seek(frame)
    left, upper, right, lower = im.getbbox()
    dx = (left - 100)//2
    dy = (upper - 100)//2
    if cx:
        draw.point([cx, cy])
    cx += dx
    cy += dy
    if dx == dy == 0:
        cx += 25
        cy = 100
new.show()



'''
a = """
18 What are some important qualities
of a good supervisor (boss)? Use specific details andexamples to explain why these qualities are important.

to be a good supervisor, there are some essentional characristics that he or she
has to have. these qualities are communication skills, management skills and
great knowledge of giving instructions.

for communications skills, a good leader or supervisor should be able to talk to its
own employees about what is good and what is wrong. for example, if there is a
paperwork that need to submit tomorrow, and the person who supposed to do this failed
to do it, then the boss havs to talk with him about the problem. After this talking,
the employee will realized the seriousness of the problem and will take care of what
he is going to do in the future.

the second thing is about the management skills. a good supervisor should be able to
tell who is good at what and send them to do things that they are good at. In this
way, people (employee) will do their job more efficiently and the company or institution
will benefits form it most

Last but not least, the knowledge of giving the instructions. It is important for a
boss to gives instructions to his employees. To be specific, in the school, teachers
are the bosses of the students, and whenever the students have the questions to ask
teacher, the teacher should be able to tell them, this is saying that teacher (boss)
should pocess such knowledge to use its employees right.

in a nutshell, thto be a good boss, it is very important to to pocesse these qualities,
they are communication skills, management skills and great knowledge of giving
instructions. And these skills in return will have good influence to making a good boss.
"""
print len(a.split())
'''
