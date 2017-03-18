import Image

def search(maze, tree):
    dirs = (0,1), (0,-1), (1,0), (-1,0)
    wall = (255,) * 4
    w,h = maze.size

    maze.putpixel((1, h-1), wall) # Wall off exit
    maze.putpixel((w-2, 0), wall) # Wall off entrance
    queue = [(1, h-2)]            # Start at exit
    tree[queue[0]] = 'exit'
    
    while queue:
        pos = queue.pop(0)
        for d in dirs:
            new_pos = pos[0] + d[0], pos[1] + d[1]
            if not tree.has_key(new_pos) and maze.getpixel(new_pos) != wall:
                tree[new_pos] = pos
                
                queue.append(new_pos)







maze = Image.open('maze.png')
tree = {}
search(maze, tree)
w = maze.size[0]
path = []
pos = (w-2,1)
while pos != 'exit':
    path.append(chr(maze.getpixel(pos)[0]))
    
    pos = tree[pos]
pos = (w-2,1)
while pos != 'exit':
    maze.putpixel(pos, (0,255,)*2)
    pos = tree[pos]

maze.save('maze-solved.png')

mazezip = ''.join(path[::2])
open('maze.zip','w').write(mazezip)
