import os

os.system("tput setaf 3")
print("\t\t\t\tWelcome to Hadoop Menu !!")
os.system("tput setaf 7")
print("--------------------------------------------------------------------------------")

r=input("Where to want to run this menu? (local/remote) :")
print(r)

def hdfs():
	dndir = input("Enter directory name u want to create for datanode:")
	print(dndir)

	os.system("echo \<configuration\> >> hdfs-site.xml")
	os.system("echo \<property\> >> hdfs-site.xml")
	os.system("echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml")
	os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(dndir))
	os.system("echo \<\/property\> >> hdfs-site.xml")
	os.system("echo \<\/configuration\> >> hdfs-site.xml")
	os.system("scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ip))
	os.system("rm -rf hdfs-site.xml")

def core():
	nn_ip = input("Enter Namenode ip and hadoop port eg. hdfs://1.2.3.4:9000:")
	print(nn_ip)

	os.system("echo \<configuration\> >> core-site.xml")
	os.system("echo \<property\> >> core-site.xml")
	os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
	os.system("echo \<value\>{}\<\/value\> >> core-site.xml".format(nn_ip))
	os.system("echo \<\/property\> >> core-site.xml")
	os.system("echo \<\/configuration\> >> core-site.xml")
	os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
	os.system("rm -rf core-site.xml")

print("""
\n
Press 0 : Namenode/Datanode hdfs configuration
Press 1 : Namenode/Datanode core configuration
Press 2 : Formatting in Namenode
Press 3 : Start service
Press 4 : Check jps
Press 5 : Report
Press 6 : Show Python Code
Press 7 : Exit the Program
""")

while True:
	if r=="local":
		ch = input("Enter ur choice :")
		print(ch)

		if int(ch) == 0:
			os.system("vi /etc/hadoop/hdfs-site.xml")
			
		elif int(ch) == 1:
			os.system("vi /etc/hadoop/core-site.xml")

		elif int(ch) == 2:
			os.system("hadoop namenode -format")

		elif int(ch) == 3:
			os.system("hadoop-daemon.sh start namenode")

		elif int(ch) == 4:
			os.system("jps")

		elif int(ch) == 5:
			os.system("hadoop dfsadmin -report")

		elif int(ch) == 6:
			os.system("vi hadoop_menu.py")

		elif int(ch) == 7:
			os.system("exit")

		else:
			print("not supported")

 
	elif r=="remote":
		ip = input("Enter remote ip :")
		print(ip)

		while True:
			ch = input("Enter ur choice :")
			print(ch)

			if int(ch) == 0:
				hdfs()

			elif int(ch) == 1:
				core()

			elif int(ch) == 3:
				os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))

			elif int(ch) == 4:
				os.system("ssh {} jps".format(ip))

			elif int(ch) == 5:
				os.system("ssh {} hadoop dfsadmin -report".format(ip))
			
			elif int(ch) == 7:
				os.system("ssh {} exit".format(ip))

			else:
				print("not supported")
		
else: 
	print("not supported login...")
