import sys
def ANU(user_name):
    if user_name not in users:
        friendships.append([user_name,[]])
        users.append(user_name)
        output.write("User '"+user_name+"' has been added to the social network successfully\n")
    else:
        output.write("ERROR: Wrong input type! for 'ANU'! -- This user already exists!!\n")
def DEU(user_name):
    if user_name in users:
        for i in range(len(users)):
            try:
                friendships[i][1].remove(user_name)
            except:
                continue
        for j in range(len(users)):
            try:
                if friendships[j][0]==user_name:
                    friendships.remove([user_name,friendships[j][1]])
            except:
                continue
        users.remove(user_name)
        output.write("User '"+user_name+"' and his/her all relations have been deleted successfully\n")
    else:
        output.write("ERROR: Wrong input type! for 'DEU'!--There is no user named "+user_name+"\n")
def ANF(domain,target):
    if domain not in users and target in users:
        output.write("ERROR: Wrong input type! for 'ANF'!--No user named '"+domain+"' found!!\n")
    elif domain in users and target not in users:
        output.write("ERROR: Wrong input type! for 'ANF'!--No user named '" + target + "' found!!\n")
    elif domain not in users and target not in users:
        output.write("ERROR: Wrong input type! for 'ANF'!--No user named '"+domain+ "' and '"+target+"' found!\n")
    elif target in friendships[users.index(domain)][1]:
        output.write("ERROR: A relation between '"+domain+"' and '"+target+"' already exists!!\n")
    else:
        friendships[users.index(domain)][1].append(target)
        friendships[users.index(target)][1].append(domain)
        output.write("Relation between '"+domain+"' and '"+target+"' has been added successfully\n")
def DEF(domain,target):
    if domain not in users and target in users:
        output.write("ERROR: Wrong input type! for 'DEF'!--No user named '"+domain+"' found!!\n")
    elif domain in users and target not in users:
        output.write("ERROR: Wrong input type! for 'DEF'!--No user named '" + target + "' found!!\n")
    elif domain not in users and target not in users:
        output.write("ERROR: Wrong input type! for 'DEF'!--No user named '"+domain+ "' and '"+target+"' found!\n")
    elif target not in friendships[users.index(domain)][1]:
        output.write("ERROR: No relation between '"+domain+"' and '"+target+"' found!!\n")
    else:
        friendships[users.index(domain)][1].remove(target)
        friendships[users.index(target)][1].remove(domain)
        output.write("Relation between '"+domain+"' and '"+target+"' has been deleted successfully\n")
def CF(user_name):
    if user_name in users:
        output.write("User '"+user_name+"' has "+str(len(friendships[users.index(user_name)][1]))+" friends\n")
    else:
        output.write("ERROR: Wrong input type! for 'CF'!--No user named '"+user_name+"' found!\n")
def FPF(user_name,max_distance):
    if user_name not in users and (max_distance>3 or max_distance<1):
        output.write("ERROR: Wrong input type! for 'FPF'!--No user named '"+user_name+"' found!\n")
        output.write("ERROR: Maximum distance must be between 1(included) and 3(included)!\n")
    elif user_name not in users:
        output.write("ERROR: Wrong input type! for 'FPF'!--No user named '" + user_name + "' found!\n")
    elif max_distance>3 or max_distance<1:
        output.write("ERROR: Maximum distance must be between 1(included) and 3(included)!\n")
    else:
        possiblelist = []
        if max_distance==1:
            for i in friendships[users.index(user_name)][1]:
                possiblelist.append(i)
        elif max_distance==2:
            for i in friendships[users.index(user_name)][1]:
                possiblelist.append(i)
                for j in friendships[users.index(i)][1]:
                    possiblelist.append(j)
        elif max_distance==3:
            for i in friendships[users.index(user_name)][1]:
                possiblelist.append(i)
                for j in friendships[users.index(i)][1]:
                    possiblelist.append(j)
                    for k in friendships[users.index(j)][1]:
                        possiblelist.append(k)
        possiblelist = list(dict.fromkeys(possiblelist))
        while user_name in possiblelist:
            possiblelist.remove(user_name)
        possiblelist.sort()
        possiblestr=str(possiblelist)
        temp_possiblestr=possiblestr.replace("[","{")
        possiblestr=temp_possiblestr.replace("]","}")
        output.write("User '" + user_name + "' have " + str(len(possiblelist)) + " possible friends when maximum distance is " + str(max_distance)+"\n")
        output.write("These possible friends: "+ possiblestr + "\n")
def SF(user_name,MD):
    if user_name not in users and (MD<1 or MD>4):
        output.write("Error: Wrong input type! for 'SF'!--No user named '"+user_name+"' found!!\n")
        output.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")
    elif user_name not in users:
        output.write("Error: Wrong input type! for 'SF'!--No user named '" + user_name + "' found!!\n")
    elif MD<1 or MD>4:
        output.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")
    else:
        MD_1,MD_2,MD_3,MD_4,full_list,suggestlist=[],[],[],[],[],[]
        for i in friendships[users.index(user_name)][1]:
            for j in friendships[users.index(i)][1]:
                full_list.append(j)
        full_list.sort()
        while user_name in full_list:
            full_list.remove(user_name)
        amount={i:full_list.count(i) for i in full_list}
        for i in amount:
            if amount[i]>=MD:
                suggestlist.append(i)
            if amount[i]==1:
                MD_1.append(i)
            elif amount[i]==2:
                MD_2.append(i)
            elif amount[i]==3:
                MD_3.append(i)
            else:
                MD_4.append(i)
        str_md1,str_md2,str_md3,str_md4,str_suggest=str(MD_1),str(MD_2),str(MD_3),str(MD_4),str(suggestlist)
        temp_1=str_md1.replace("[","")
        str_md1=temp_1.replace("]","")
        temp_2 = str_md2.replace("[", "")
        str_md2 = temp_2.replace("]", "")
        temp_3 = str_md3.replace("[", "")
        str_md3 = temp_3.replace("]", "")
        temp_4 = str_md4.replace("[", "")
        str_md4 = temp_4.replace("]", "")
        temp_suggest = str_suggest.replace("[", "")
        str_suggest = temp_suggest.replace("]", "")
        output.write("Suggestion List for '"+user_name+"' (when MD is "+str(MD)+"):\n")
        if MD==1 and len(MD_1)>0:
            output.write(user_name+" has 1 mutual friend with "+str_md1+"\n")
        if (MD==1 or MD==2) and len(MD_2)>0:
            output.write(user_name + " has 2 mutual friends with " + str_md2+"\n")
        if (MD==1 or MD==2 or MD==3) and len(MD_3)>0:
            output.write(user_name + " has 3 mutual friends with " + str_md3+"\n")
        if (MD==1 or MD==2 or MD==3 or MD==4) and len(MD_4)>0:
            output.write(user_name + " has 4 mutual friends with " + str_md4+"\n")
        output.write("The suggested friends for '"+user_name+"':"+str_suggest+"\n")
friendships,users=[],[]
smn,commands=sys.argv[1]+"/smn.txt",sys.argv[2]+"/commands.txt"
output= open("output.txt","w")
with open(smn) as smn_txt:
    templist=smn_txt.readlines()
    for i in templist:
        if i.endswith("\n"):
            x=templist.index(i)
            templist[x]=i[:-1]
    for i in templist:
        x=templist.index(i)
        templist[x]=i.rstrip()
    for i in templist:
        y=i.index(":")
        personallist=[i[:y],i[y+1:].split(" ")]
        friendships.append(personallist)
        users.append(i[:y])
with open(commands) as commands_txt:
    templist=commands_txt.readlines()
    for i in templist:
        if i.endswith("\n"):
            x=templist.index(i)
            templist[x]=i[:-1]
    for i in templist:
        x=templist.index(i)
        templist[x]=i.rstrip()
    for i in templist:
        if i.startswith("ANU"):
            ANU(i[4:])
        elif i.startswith("DEU"):
            DEU(i[4:])
        elif i.startswith("ANF"):
            x=i.split(" ")
            ANF(x[1],x[2])
        elif i.startswith("DEF"):
            x=i.split(" ")
            DEF(x[1],x[2])
        elif i.startswith("CF"):
            CF(i[3:])
        elif i.startswith("FPF"):
            x=i.split(" ")
            try:
                FPF(x[1],int(x[2]))
            except:
                output.write("Error: Wrong input type! for 'SF'!--No user named '" + x[1] + "' found!!\n")
        elif i.startswith("SF"):
            x=i.split(" ")
            try:
                SF(x[1],int(x[2]))
            except:
                output.write("Error: Wrong input type! for 'SF'!--No user named '"+x[1]+"' found!!\n")
        else:
            output.write("You have entered an Incorrect Command!\n")
output.close()