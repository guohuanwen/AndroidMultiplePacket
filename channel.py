import os
import shutil

# replace_channel(渠道名称,需要编译的文件夹):
def replace_channel(channel,filename):
    if not os.path.exists(filename+'\AndroidManifest.xml'): # 看一下这个文件是否存在
        print("没有文件")
        exit()       #不存在就退出

    shutil.copyfile(filename+'\AndroidManifest.xml','AndroidManifest.xml')
    lines = open('AndroidManifest.xml').readlines()  #打开文件，读入每一行
    fp = open(filename+'\AndroidManifest.xml','w')  #打开你要写得文件
    fp.truncate()
    for s in lines:
    # replace是替换，write是写入
        fp.write( s.replace('UMENG_CHANNEL_VALUE',channel))    
    fp.close()  # 关闭文件
    command = 'apktool b ' + filename + ' -o  output\\' + channel+ '.apk'
    os.system(command)
    #sign_command = "java -jar signapk.jar testkey.x509.pem testkey.pk8  "+" output\\" + channel+ ".apk "+ " output\\" + channel+ "_sign.apk "
    #os.system(sign_command)
    shutil.copyfile('AndroidManifest.xml',filename+'\AndroidManifest.xml')

#packet_apk （文件名，解包后的文件夹名称）
def packet_apk(apk_name,filename):
    if os.path.exists(filename): # 看一下这个文件是否存在
        shutil.rmtree(filename)  #存在直接删除掉
        
    #反编译命令
    command = "apktool d  "+apk_name+".apk " + " -o "+filename
    os.system(command)
    #替换渠道号
    lines = open('channel.txt').readlines()  #打开文件，读入每一行
    for s in lines:
        s=s.strip('\n')#去掉换行符
        replace_channel(str(s),filename)
    

if __name__=="__main__":
    packet_apk("wepie","debug_apk")
    
    
