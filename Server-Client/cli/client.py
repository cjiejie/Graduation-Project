#! /usr/bin/python
def tcpClient():  
	BUFSIZE = 1024
	FILEINFO_SIZE=struct.calcsize('128s32sI8s')
	clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	addr=raw_input("please input the server ip")
	clisock.connect((addr, 9527))  
	############################################
	print " '1':decode dimensions "
	print " '2':create a dimensions imeage"
	print " 's':stop the server "
	command=raw_input("command:")
	clisock.sendall(command)  
	if command=='1':
		dat = clisock.recv(1024)  
		print dat  
	elif command=='2':
		print "please input information in dimensions"
		clisock.sendall(raw_input(""))
		####
		fhead = clisock.recv(FILEINFO_SIZE)
		filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)
		#print filename,temp1,filesize,temp2
		print filename,len(filename),type(filename)
		print filesize
		filename = 'new_'+filename.strip('\00') 
		fp = open(filename,'wb')
		restsize = filesize
		print "rec... "
		while 1:
			if restsize > BUFSIZE:
				filedata = clisockrecv(BUFSIZE)
			else:
				filedata = clisock.recv(restsize)
			if not filedata: break
			fp.write(filedata)
			restsize = restsize-len(filedata)
			if restsize == 0:
				break
		print "rec ok"
		fp.close()
		clisock.close()
		print "close"
		####
#		dat = clisock.recv(1024)      
     ###########################################      
if __name__ == "__main__":  
	import socket,struct
	tcpClient()  
