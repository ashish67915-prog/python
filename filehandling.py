#if file is not open

# f = open("sample.txt","w")
# f.write("hello world")
#why we use close file
#1)memory space ke liye 2)safety so that no can use directly
# f.close()
#this will not work because file is closed now.
# f.write("how are you")


#if you have to write in more than one line
# f = open("zero.txt","w")
# f.write("Hello dostoo")
# f.write("\nkaise ho sabhi")
# f.close()


#if file is already exist
#jb hmm existing file me write mode("w") ka estmal karte hai to existing data remove ho jata hai aur new data write ho jata hai.
# f = open("sample.txt","w")
# f.write("hello dostoo")
# f.close()



#how this open() works?
#when we use open then a buffer create in a RAM and then jb tak operation hoga tb tk buffer me kaam hoga fir kaam hone ke baad buffer close ho jata hai



#if you want that the existing file data will not remove and i write anything on this existing file then use append mode

# f = open("zero.txt","a")
# f.write("\nI am fine")
# f.close()


#for write lines
# L = ["will you submit your assignment\n","yes i can\n","ooh that's great"]
# f = open("sample.txt","w")
# f.writelines(L)
# f.close()



#read a file using ->open()
#read() ye puri file ko ek baar me read karleta hai
# f = open("sample.txt","r")
# s = f.read()
# print(s)
# f.close()


#agar upto n char tak hi read karna hai
# f = open("sample.txt","r")
#here we specify that you only read upto 10 characters
# s = f.read(10)
# print(s)
# f.close()

#readline()->reading line by line
#here we use end = ""  because print also excecute new line and readline also excute new line so there is a one line gap occur in between lines so we use end to remove this one line gap.
# f = open("zero.txt","r")
# print(f.readline(),end = "")
# print(f.readline(),end = "")
# f.close()


#reading entire using readline()
# f = open("zero.txt","r")

# while True:
#     data = f.readline()

#     if data == "":
#         break
#     else:
#         print(data,end = "")

# f.close()
