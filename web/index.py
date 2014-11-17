import web,os,time,zbar_t,gl,creat_Dimensions,StringIO
from web import form

render = web.template.render("templates/")

urls = (
    '/', 'index',
	'/control','control',
	'/decode', 'decode',
	'/create', 'create',
	'/ans','ans',
	'/show','show',
)
app = web.application(urls, globals())
login = form.Form(
	form.Textbox('username'),
	form.Password('password'),
	form.Button('Login'),
	validators = [form.Validator("passwd error.", lambda i: i.password == '123456')]
)
cre = form.Form(
	form.Textbox('Text',description="Text"),
	form.Button('create'),
)
class index:

	def GET(self):
		f=login()
		return render.formtest(f)
	def POST(self):
		f=login()
		if not f.validates():
			return render.formtest(f)
		else:
			web.seeother('/control')
class control:
	def GET(self):
		return render.con()
class decode:
	def GET(self):
		return render.decode()
class ans:
	def GET(self):
		zbar_t.zbar_decode()
		im=gl.zbar_ret
		return render.ans(im)
class create:
	def GET(self):
		f=cre()
		print "goto get"
		return render.create(f)
	def POST(self):
		f=cre()
		print "goto post"
		data=web.input()
		print data.Text
		if not f.validates():  
			return 'please input you Text'  
		else:  
			creat_Dimensions.Encode(data.Text)
			os.system('mv imeage.png static/')
			web.seeother('static/show.html')
class show:
	def GET(self):
		return render.show()
if __name__ == "__main__":
	web.internalerror = web.debugerror
	app.run()

