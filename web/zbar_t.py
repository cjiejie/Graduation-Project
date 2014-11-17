#!/usr/bin/python  
from sys import argv  
import zbar,os,gl
def my_handler(proc, image, closure):  
	for symbol in image:  
		if not symbol.count: 
			gl.zbar_ret=symbol.data 
def zbar_decode():
	proc = zbar.Processor()  
	proc.parse_config('enable')  
	device = '/dev/video0'  
#	if len(argv) > 1:  
#		device = argv[1]  
	proc.init(device)    
	proc.set_data_handler(my_handler)   
	proc.visible = 0 
	proc.active = True  
	try:
		proc.process_one()
	except zbar_flag:  
		pass
