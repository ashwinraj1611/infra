import os,errno,shutil


path1 = os.environ['HOME'] + "/Desktop/"
path2 = os.environ['HOME'] + "/Documents/"
print path1
print path2

def extract(arr_list):
	for i in arr_list:
		x = i.split("/Desktop/",1)[1]
		src = path1+x
		#print src
		if os.path.isdir(i):
			print "Transfering...."
			#print x

		else:

			if '.' in x:
				#x = x+".txt"
			#if no file extension found then .txt is asuumed	

				ind = x.rfind('.')
				x = x[ind+1:]
			
				
				
			#print x	
				try:
					os.makedirs(path2+x)
				except OSError as e:
					if e.errno != errno.EEXIST:
						raise

				dest = path2+x+"/"
				#print dest
				shutil.move(src,dest)		


		#	if not os.path.exists(path1+x):
				
				
				





def main():
	import glob
	path5 = os.environ['HOME'] + "/Desktop/*"
	arr_list = glob.glob(path5)
	extract(arr_list)

if __name__ == "__main__":
	main()