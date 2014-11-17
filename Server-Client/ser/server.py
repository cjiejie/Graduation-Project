#! /usr/bin/python
def tcpServer():  
	srvsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)  
	srvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	srvsock.bind(('', 9527))  
	srvsock.listen(5)  
      
	while True:  
		clisock, (remoteHost, remotePort) = srvsock.accept()  
		print " connected by [%s:%s]" % (remoteHost, remotePort)  
		#######################################
		dat = clisock.recv(1024)
		gl.server_rec=dat
		if dat=='1':
			print "decode..."
			zbar_t.zbar_decode()
			dat='decode is :'+gl.zbar_ret
			clisock.sendall(dat)  
			print "ok"
		elif dat=='2':
			print "wait input information"
			create_dat = clisock.recv(1024)
			print "create a dimensions,name is dimensions.png"
			creat_Dimensions.Encode(create_dat)
			print "creat ok"
			###
			BUFSIZE = 1024
			filename = 'dimensions.png'
			FILEINFO_SIZE=struct.calcsize('128s32sI8s')
			fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)
			clisock.send(fhead)
			fp = open(filename,'rb')
			while 1:
				filedata = fp.read(BUFSIZE)
				if not filedata: break
				clisock.send(filedata)
			print "ok"
			fp.close()
			clisock.close()
			print "close..."
			###
		elif dat=='s':
			srvsock.close()
			sys.exit()
		#######################################
		clisock.close()  
      
if __name__ == "__main__":  
	import socket,os,gl,sys,traceback,zbar_t,creat_Dimensions,struct
	try:
		tcpServer() 
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
