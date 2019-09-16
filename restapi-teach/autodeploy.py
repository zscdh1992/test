targetMachine_host = "192.168.3.15"
targetMachine_loginname = "stt5"
targetMachine_loginpass = "stt5200"

build_dir = 'c:/Program Files (x86)/Jenkins/workspace/songqin'
root_dir = 'd:/tmp/jenkinsbuild'
zip_dir = root_dir + '/restapi-teach'
zip_name = 'restapi-teach'
zip_file = root_dir +'/restapi-teach.zip'

import paramiko,sys
import os,shutil

if os.path.exists(zip_dir):
    shutil.rmtree(zip_dir)


if os.path.exists(zip_file):
    os.remove(zip_file)

os.makedirs(zip_dir)
shutil.copytree(build_dir+'/backend', zip_dir+'/backend')
shutil.copytree(build_dir+'/static', zip_dir+'/static')
shutil.copy(build_dir+'/run.sh', zip_dir+'/run.sh')

shutil.make_archive(zip_dir, 'zip', root_dir,zip_name)


# os._exit(0)

#创建SSHClient 实例对象
ssh = paramiko.SSHClient()

#调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程机器  地址、端口、用户名密码
ssh.connect(targetMachine_host,
            22,
            targetMachine_loginname,
            targetMachine_loginpass)



def remoteRun(cmd,printOutput=True):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read().decode()
    errinfo = stderr.read().decode()
    if printOutput:
        print(output + errinfo)
    return  output + errinfo




#检查是否有先前的版本运行
output = remoteRun('ps -ef|grep apiteach|grep -v grep')

# 如果存在，则杀死进程
if 'python3 project/cherrypy_startup.py apiteach' in output:
    print('服务运行中，停止服务')

    parts = output.split(' ')
    print(parts)


    parts = [part for part in parts if part]
    print(parts)

    pid = parts[1]

    output = remoteRun(f'kill -9 {pid}')
    if 'python3 project/cherrypy_startup.py apiteach' in output:
        print('不能停止运行的服务！！！')
        # 退出进程
        sys.exit(3)

    else:
        print('停止成功')


print('删除原来的代码包')
remoteRun('rm -f restapi-teach.zip')

print('上传安装包')
sftp = ssh.open_sftp()
sftp.put(zip_file, '/home/stt5/restapi-teach.zip')
sftp.close()


print('备份原来的安装目录')
remoteRun('rm -rf restapi-teach.bak;mv restapi-teach restapi-teach.bak')


print('解压安装包...',end='')
remoteRun('unzip restapi-teach.zip',printOutput=False)
print('ok')


print('运行')
remoteRun('cd restapi-teach;chmod +x run.sh;dos2unix run.sh; ./run.sh')


print('检查是否运行成功')
output = remoteRun('sleep 5;ps -ef|grep apiteach|grep -v grep')

# 如果存在，则表示运行成功
if 'python3 project/cherrypy_startup.py apiteach' in output:
    print('服务运行成功')
else:
    print('服务没有运行！！')
    sys.exit(3)
