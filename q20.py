import sys
with open("q20.txt") as f:
          content = f.readlines()
content = [x.strip() for x in content]
particle_pos = []
particle_vel = []
particle_acc = []
dead = []
for i in content:
    temp = i.split(', ')
    temp0 = temp[0]
    temp0 = temp0[3:len(temp0)-1]
    temp0 = temp0.split(',')
    temp0 = (int(temp0[0]), int(temp0[1]), int(temp0[2]))
    particle_pos.append(temp0)

    temp0 = temp[1]
    temp0 = temp0[3:len(temp0)-1]
    temp0 = temp0.split(',')
    temp0 = (int(temp0[0]), int(temp0[1]), int(temp0[2]))
    particle_vel.append(temp0)

    temp0 = temp[2]
    temp0 = temp0[3:len(temp0)-1]
    temp0 = temp0.split(',')
    temp0 = (int(temp0[0]), int(temp0[1]), int(temp0[2]))
    particle_acc.append(temp0)
def get_smallest():
    smallest = sys.maxsize
    smallest_index = -1
    for i in range(len(particle_pos)):
        temp = abs(particle_pos[i][0]) + abs(particle_pos[i][1]) + abs(particle_pos[i][2])
        if temp < smallest:
            smallest = temp
            smallest_index = i
    return smallest_index

def simulate(n):
    for t in range(n):
        crash_zone = {}
        for i in range(len(particle_pos)):
            """ faster way to solve
            a = particle_pos[i][0] + particle_vel[i][0] * n + particle_acc[i][0] * n * (n+1) / 2
            b = particle_pos[i][1] + particle_vel[i][1] * n + particle_acc[i][1] * n * (n+1) / 2
            c = particle_pos[i][2] + particle_vel[i][2] * n + particle_acc[i][2] * n * (n+1) / 2
            particle_pos[i] = (a,b,c)
            """
            if i in dead:
                pass
            a = particle_vel[i][0] + particle_acc[i][0]
            b = particle_vel[i][1] + particle_acc[i][1]
            c = particle_vel[i][2] + particle_acc[i][2]
            particle_vel[i] = (a,b,c)

            a = particle_pos[i][0] + particle_vel[i][0]
            b = particle_pos[i][1] + particle_vel[i][1]
            c = particle_pos[i][2] + particle_vel[i][2]    
            particle_pos[i] = (a,b,c)
            if particle_pos[i] in crash_zone:
                crash_zone[particle_pos[i]].append(i)
            else:
                crash_zone[particle_pos[i]] = [i]
        #print(crash_zone)
        
        for j in crash_zone:
            if len(crash_zone[j]) > 1:
                print("crash at time ", t)
                for k in crash_zone[j][::-1]:
                    #print("crash at ", j, "   ", crash_zone[j])
                    #print("removing ", k)
                    dead.append(k)
    print(len(dead), "Particles collided away.")
                        
